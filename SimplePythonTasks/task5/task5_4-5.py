letter = '''Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

letter_formated = letter.format(salutation = "Mr.",
                                name = "Cat",
                                product = "Electro-mouse",
                                verbed = "exploded",
                                room = "bathroom",
                                animals = "real mice",
                                amount = "10$",
                                percent = 0.0001,
                                spokesman = "John",
                                job_title = "Manager")
print(letter_formated)
