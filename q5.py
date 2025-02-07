gmail = input( "Enter the email address here: " )

domain = gmail[gmail.index ('@') + 1:]

print( " The domain for your email is : ", domain )