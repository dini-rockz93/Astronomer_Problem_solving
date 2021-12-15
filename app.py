from models import PRODUCTS

def main():
    
    basket = PRODUCTS()
    print("Enter the products")
    elements = input().split(',')
    
    # ensure the element values are in upper case
    # leading and trailing spaces are trimmed

    upper_convert = lambda x: x.strip().upper()
    elements = list(map(upper_convert, elements))
    
    for val in elements:
        status = basket.add(val)
        if status == -1:
            print('%s item not present'.format(val))
          
    print(basket.total())
    
if __name__ == '__main__':
    main()