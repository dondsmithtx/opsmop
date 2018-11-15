from opsmop.providers.provider import Provider

class Debug(Provider):

    def quiet(self):
        return True

    def verb(self):
        return "debugging..."

    def skip_plan_stage(self):
        return True
 
    def apply(self):
        
        variables = self.resource.get_variables()

        for vname in self.variable_names:
            if vname in variables:
                self.echo("%s = %s" % (vname, variables[vname]))
            else:
                self.echo("%s is not defined" % vname)

        for (k, expr) in self.evals.items():
            actual = expr
            if issubclass(v, Condition):
                 actual = expr.evaluate(self.resource)
            self.echo("%s => %s" % (k, actual))
          
        return self.ok()