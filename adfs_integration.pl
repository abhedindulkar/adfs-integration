use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request;

sub authenticate_with_adfs {
    my ($username, $password, $adfs_url) = @_;

    # Construct the SOAP request payload
    my $soap_request = <<"END_SOAP";
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <RequestSecurityToken xmlns="http://docs.oasis-open.org/ws-sx/ws-trust/200512">
            <TokenType>urn:oasis:names:tc:SAML:1.0:assertion</TokenType>
            <RequestType>http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue</RequestType>
        </RequestSecurityToken>
    </s:Body>
</s:Envelope>
END_SOAP

    # Create a user agent
    my $ua = LWP::UserAgent->new;

    # Create an HTTP request
    my $request = HTTP::Request->new(POST => $adfs_url);
    $request->header('Content-Type' => 'text/xml; charset=utf-8');
    $request->header('SOAPAction' => 'http://docs.oasis-open.org/ws-sx/ws-trust/200512/RST/Issue');
    $request->content($soap_request);
    $request->authorization_basic($username, $password);

    # Send the request
    my $response = $ua->request($request);

    # Check the response
    if ($response->is_success) {
        return $response->decoded_content; # Return the security token
    } else {
        return "Error: " . $response->status_line;
    }
}

# Example usage
my $username = "example_user";
my $password = "example_password";
my $adfs_url = "https://adfs.example.com/adfs/services/trust/13/usernamemixed";

my $token = authenticate_with_adfs($username, $password, $adfs_url);

print "$token\n";

