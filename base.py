import requests
from requests.auth import HTTPBasicAuth

def authenticate_with_adfs(username, password, adfs_url):
    """
    Authenticate with ADFS and retrieve a security token.

    :param username: The username of the user to authenticate.
    :param password: The password of the user to authenticate.
    :param adfs_url: The URL of the ADFS server.
    :return: Security token or error message.
    """
    try:
        # Construct the SOAP request payload
        soap_request = f"""
        <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\">
            <s:Body>
                <RequestSecurityToken xmlns=\"http://docs.oasis-open.org/ws-sx/ws-trust/200512\">
                    <TokenType>urn:oasis:names:tc:SAML:1.0:assertion</TokenType>
                    <RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType>
                </RequestSecurityToken>
            </s:Body>
        </s:Envelope>
        """

        # Send the SOAP request to the ADFS server
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'http://docs.oasis-open.org/ws-sx/ws-trust/200512/RST/Issue'
        }
        response = requests.post(adfs_url, data=soap_request, headers=headers, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful
        if response.status_code == 200:
            return response.text  # Return the security token
        else:
            return f"Error: {response.status_code} - {response.reason}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    username = "example_user"
    password = "example_password"
    adfs_url = "https://adfs.example.com/adfs/services/trust/13/usernamemixed"

    token = authenticate_with_adfs(username, password, adfs_url)
    print(token)