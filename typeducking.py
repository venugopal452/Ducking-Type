class game:
    def cricket(self):
        print("eleven players required")
        print("two team must")
        print("only one win at the end")

class college:
    def student(self, ide):
        print("books are there")
        print("so many classes")
        print("so much fun")
        ide.cricket()

ide = game()
col = college()
col.student(ide)

# ide : integrated development environment, ducking type is duck use to call the method , the above code "ide" is the ducking type
# we can change the "ide" as other names as we wish.    