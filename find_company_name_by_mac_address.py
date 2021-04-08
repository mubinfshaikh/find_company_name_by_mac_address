# imported sys module for command line argument
import sys
# imported requests for REST GET API call to the api.macaddress.io
import requests


# create a class to bind the all functions (as here not required but for future scope)
class MacAddress:
    # Set API key (taken API key from api.macaddress.io)
    API_KEY = "at_k64Bzn7pziWSCHg7ixvRNcP33uzzp"

    def get(self, mac_address):
        try:
            # generated request URL combining API key and MAC address
            request_url = "https://api.macaddress.io/v1?apiKey={API_KEY}&output=json&search={mac_address}".format(API_KEY = self.API_KEY, mac_address = mac_address)
            # Sent get request to the api.macaddress.io
            request_response = requests.get(request_url)
            # converted response in JSON and send to mother method
            return True, request_response.json()
        except Exception as e:
            # in case of exception
            return False, {"exception" : str(e)}


# invoke the python program
if __name__ == "__main__":
    # Check the MAC address is given or not
    command_line_arguments_count = len(sys.argv)
    if command_line_arguments_count > 1:
        # create a object of a class for calling method
        obj_mac_address = MacAddress()
        # by default first argument is program name so excluded the first argument using slicing
        command_line_arguments_list = sys.argv[1:]
        # iterate over the list if more than one MAC address given as an input
        for loop_index, mac_address in enumerate(command_line_arguments_list):
            mac_address_status, mac_address_data = obj_mac_address.get(mac_address)
            if mac_address_status:
                print("{loop_index}. The MAC address {mac_address} is associated with company name - {company_name}.".format(loop_index = loop_index + 1, mac_address = mac_address, company_name = mac_address_data['vendorDetails']['companyName']))
            else:
                print(mac_address_data)
    else:
        print("You are not provided any MAC address, please provide MAC address via command line argument ...")


# python command to execute via terminal (ubuntu)
# python3 find_company_name_by_mac_address.py 44:38:39:ff:ef:57 44:38:39:ff:ef:58
