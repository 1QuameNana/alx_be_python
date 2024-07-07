FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =  9/5
def convert_to_celsius(fahrenheit):
    'takes a user input and converts it from fahrenheit to celsius'
    celsius = (fahrenheit-32) *FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
    
def convert_to_fahrenheit(celsius):
    'takes a user input for a celsius to fahrenheit conversion'
    fahrenheit =  (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
        temp = float(input('Enter the temperature to convert: '))
        if unit == 'C':
            celsius = convert_to_celsius(temp)
            print(f'{temp}°F is: {celsius}°C')
            pass
        elif unit =='F':
            fahrinheit = convert_to_fahrenheit(temp)
            print(f'{temp}°C is: {fahrinheit}°F')
        else:
            print(f'{unit} is an invalid unit of measure')
            
if __name__ == "__main__":
    main()
