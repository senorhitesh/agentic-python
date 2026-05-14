class Chai:
    def __init__(self, type_,strength) -> None:
        self.type = type_
        self.strength = strength ;

# Code Duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, s_level) -> None:
#         self.type = type_
#         self.strength = strength
#         self.s_level = s_level;


# Explicit
# class GingerChai(Chai):
#     def __init__(self, type_, strength, s_level) -> None:
#         Chai.__init__(self,type_, strength)
#         self.s_level = s_level

# Super

class GigerChai(Chai):
    def __init__(self, type_, strength,s_level) -> None:
        super().__init__(type_, strength)
        self.s_level = s_level
