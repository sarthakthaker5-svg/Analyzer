import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    @classmethod
    def project_info(cls):
        print("\nWelcome to the NumPy Analyzer!")
        print("==========================")

    @staticmethod
    def input_elements(size):
        values = list(map(int, input(f"Enter {size} elements for the array separated by space: ").split()))
        return values

    def __validate_array(self):
        if self.array is None:
            print("No array exists! Create array first.")
            return False
        return True

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter the size of array: "))
            data = self.input_elements(n)
            self.array = np.array(data)

        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            size = rows * cols

            data = self.input_elements(size)
            self.array = np.array(data).reshape(rows, cols)

        elif choice == 3:
            x = int(input("Enter the Depth: "))
            y = int(input("Enter the number of rows: "))
            z = int(input("Enter the number of columns: "))

            size = x*y*z
            data = self.input_elements(size)
            self.array = np.array(data).reshape(x,y,z)

        print("\nArray created successfully:")
        print(self.array)

    def indexing_slicing(self):
        
        if not self.__validate_array():
            return
        
        while True:

            print("Choose an option:")
            print("\n1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            
            choice = int(input("Enter your choice: "))
            if choice == 1:
                
                if self.array.ndim == 1:
                    i = int(input("Index: "))
                    print("Value:", self.array[i])
                    
                elif self.array.ndim == 2:
                    r = int(input("Enter the number of rows:"))
                    c = int(input("Enter the number of columns: "))
                    print("Value:", self.array[r, c])
            
            elif choice == 2:
                
                if self.array.ndim == 1:
                    start = int(input("Start: "))
                    end = int(input("End: "))
                    print(self.array[start:end])
                    
                elif self.array.ndim == 2:
                    rs = input("Enter the row range (start:end): ")
                    cs = input("Enter the column range (start:end): ")
                    
                    r1, r2 = map(int, rs.split(":"))
                    c1, c2 = map(int, cs.split(":"))
                    
                    print(self.array[r1:r2, c1:c2])
                    
            elif choice == 3:
                print("Returning to main menu...")
                break
            
            else:
                print("Invalid choice")

    def combine_split(self):
        
        if not self.__validate_array():
            return
        
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            
            size = self.array.size
            
            data = self.input_elements(size)
            
            second = np.array(data).reshape(self.array.shape)
            
            combined = np.vstack((self.array, second))
            
            print("\nOriginal Array:")
            print(self.array)
            
            print("\nSecond Array:")
            print(second)
            
            print("\nCombined Array (Vertical Stack):")
            print(combined)
            
        elif choice == 2:
            
            try:
                
                result = np.array_split(self.array, 2)
                
                print("\nSplit Arrays:")
                
                for i, arr in enumerate(result):
                    print(f"\nPart {i+1}:")
                    print(arr)
                    
            except:
                print("Cannot split array")
                
        else:
            print("Invalid choice")

    def math_operations(self):
        if not self.__validate_array():
            return
        
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = int(input("Enter your choice: "))
        size = self.array.size
        data = self.input_elements(size)
        
        second = np.array(data).reshape(self.array.shape)
        
        print("\nOriginal Array:")
        print(self.array)
        
        print("\nSecond Array:")
        print(second)
        
        if choice == 1:
            result = self.array + second
            print("\nResult of Addition:")
            print(result)
            
        elif choice == 2:
            result = self.array - second
            print("\nResult of Subtraction:")
            print(result)

        elif choice == 3:
            result = self.array * second
            print("\nResult of Multiplication:")
            print(result)

        elif choice == 4:
            result = self.array / second
            print("\nResult of Division:")
            print(result)

        else:
            print("Invalid choice")

    def search_sort_filter(self):

        if not self.__validate_array():
            return

        print("\n1.Search a value")
        print("2.Sort the array")
        print("3.Filter values")

        choice=int(input("Choice an option: "))

        if choice==1:

            value=int(input("Enter value: "))

            pos=np.where(self.array==value)

            print("Found at:",pos)

        elif choice==2:

            print("\n1.Ascending")
            print("2.Descending")

            order=int(input("Enter your choice: "))

            if order==1:
                print("Original Array:")
                print(np.sort(self.array))

            else:
                
                print(np.sort(self.array)[::-1])

        elif choice==3:

            value=int(input("Show values greater than: "))

            print(self.array[self.array>value])

    def aggregate_functions(self):

        if not self.__validate_array():
            return

        print("\nAggregate Functions")

        print("Sum:",np.sum(self.array))
        print("Mean:",np.mean(self.array))
        print("Median:",np.median(self.array))
        print("Standard Deviation:",np.std(self.array))
        print("Variance:",np.var(self.array))

    def statistical_functions(self):

        if not self.__validate_array():
            return
        
        print("\nStatistical Functions")

        print("Minimum:",np.min(self.array))
        print("Maximum:",np.max(self.array))
        p=int(input("Enter percentile: "))
        print("Percentile:",np.percentile(self.array,p))

        print("\nCorrelation")

        size=self.array.size
        data=self.input_elements(size)
        second=np.array(data)
        flat=self.array.flatten()
        corr=np.corrcoef(flat,second)
        print(corr)

def main():

    obj=DataAnalytics()

    obj.project_info()
    while True:
        print("\nChoose an option:")
        print("1.Create a Numpy Array")
        print("2.Perform Mathematical Operations")
        print("3.Combine or Split Arrays")
        print("4.Search,Sort, or Filter Arrays")
        print("5.Compute Aggregates and Statistics")
        print("6.Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            obj.create_array()
            obj.indexing_slicing() 
            
        elif choice == 2:
            obj.math_operations()
        
        elif choice == 3:
            obj.combine_split()
            
        elif choice == 4:
            obj.search_sort_filter()
        
        elif choice == 5:
            print("\n1. Aggregates")
            print("2. Statistics")
            sub = int(input("Enter your choice: "))
            
            if sub == 1:
                obj.aggregate_functions()
                
            elif sub == 2:
                obj.statistical_functions()
            
            else:
                print("Invalid choice")
                
        elif choice == 6:
            print("\nThank you for using NumPy Analyzer! Goodbye!")
            break
        
        else:
            print("Invalid choice")

main()