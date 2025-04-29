# ADFS Integration

## Overview
This project contains a Perl script designed to integrate with Active Directory Federation Services (ADFS). The script facilitates user authentication and retrieves security tokens from the ADFS server. It is specifically designed to work with ADFS 2.0.

## What Does This Script Do?
The script uses the `SOAP::Lite` module to:
- Make SOAP requests to the ADFS server.
- Authenticate users using their credentials.
- Retrieve security tokens for authenticated users.

## Prerequisites
Before using this script, ensure you have the following:
- **Perl Installed**: Make sure Perl is installed on your system.
- **SOAP::Lite Module**: This module is required to make SOAP requests. You can install it using CPAN:
  ```bash
  cpan install SOAP::Lite
  ```
- **ADFS Server**: The script is designed to work with ADFS 2.0.

## Parameters
The script requires the following parameters to function:

### 1. `$username`
- **Description**: The username of the user to authenticate.
- **Example**: `john.doe@example.com`

### 2. `$password`
- **Description**: The password of the user to authenticate.
- **Example**: `P@ssw0rd!`

### 3. `$adfs_url`
- **Description**: The URL of the ADFS server.
- **Example**: `https://adfs.example.com/adfs/services/trust`

## How to Use the Script

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/adfs-integration.git
cd adfs-integration
```

### Step 2: Edit the Script
Open the `adfs_integration.pl` file and update the parameters with your ADFS server details:
```perl
my $username = 'your-username';
my $password = 'your-password';
my $adfs_url = 'https://your-adfs-server/adfs/services/trust';
```

### Step 3: Run the Script
Run the script using Perl:
```bash
perl adfs_integration.pl
```

## How to Create a Perl Script
If you're new to Perl, follow these steps to create and run a Perl script:

### Step 1: Install Perl
Ensure Perl is installed on your system. On most Linux distributions, Perl comes pre-installed. To check, run:
```bash
perl -v
```

### Step 2: Write Your Script
Create a new file with a `.pl` extension, for example, `example.pl`. Open it in a text editor and write your Perl code. Here's a simple example:
```perl
#!/usr/bin/perl
use strict;
use warnings;

print "Hello, World!\n";
```

### Step 3: Make the Script Executable
Make the script executable by running:
```bash
chmod +x example.pl
```

### Step 4: Run the Script
Run the script using:
```bash
./example.pl
```

## Additional Resources
- [Perl Documentation](https://perldoc.perl.org/)
- [SOAP::Lite Documentation](https://metacpan.org/pod/SOAP::Lite)
- [ADFS Overview](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview)

## Troubleshooting
If you encounter issues, check the following:
- Ensure the `SOAP::Lite` module is installed.
- Verify the ADFS server URL is correct.
- Check your username and password for accuracy.

Feel free to reach out for support or open an issue in the repository if you need further assistance.