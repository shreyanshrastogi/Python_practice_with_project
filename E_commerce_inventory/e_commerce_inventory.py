import data


def print_inventory_report():
    '''Prints selling inventory '''
    print("\n+++Daily Inventory Report+++")
    print("\n++Right now Selling++")
    for item in data.PRODUCTS:
        print(f"Now selling: {item.title()}")


def print_top_products():
    '''this prints top 3 products'''
    print("\n+++Top 3 Selling products+++")
    for index,value in enumerate(data.PRODUCTS[:3]):
        print(f"{index+1} = {value.title()}")

def get_sales_data():
    '''It returns min, max, total sales'''
    minimum_sale=min(data.SALES_NUMBERS)
    maximum_sale=max(data.SALES_NUMBERS)
    total_sale=sum(data.SALES_NUMBERS)

    return (minimum_sale,maximum_sale,total_sale)

def print_retail_prices():
    '''this prints retail prices'''
    retail_price=[i*1.5 for i in data.COSTS]
    print("\n+++Retail Pricing+++")
    for i in range(len(data.COSTS)):
        print(f"{data.PRODUCTS[i].title()}:{data.COSTS[i]:.2f}Rs --> {retail_price[i]:.2f}")


def print_store_location():
    '''print store location'''
    print("+++Store location+++\n")
    print(f"+++Report for store:{data.STORE_LOCATION}+++")


def main():
    '''main function to run this inventory report'''

    
    print_store_location()

    
    print_inventory_report()

    
    print_top_products()

    min_sale,max_sale,total_sale=get_sales_data()

    print("\n+++Sales DATA+++")

    print("\n+++Total Items Sold++")
    print(f"Total items sold(units): {total_sale}")
    print(f"Worst  selling items(units): {min_sale} of {data.PRODUCTS[data.SALES_NUMBERS.index(min_sale)]}")
    print(f"Best selling items(units): {max_sale} of {data.PRODUCTS[data.SALES_NUMBERS.index(max_sale)]}")

    print_retail_prices()






















if __name__=="__main__":
    main()





