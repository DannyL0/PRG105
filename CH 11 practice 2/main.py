from employee import ProductionWorker


def main():
    prod_worker_name = input("Enter the workers name: ")
    prod_worker_number = input("Enter the workers employee number: ")
    prod_worker_shift = input("Enter the workers shift number: ")
    prod_worker_hourly = float(input("Enter the workers hourly rate: "))
    prod_obj = ProductionWorker(prod_worker_name, prod_worker_number, prod_worker_shift, prod_worker_hourly)
    print(prod_obj.__str__())


main()
