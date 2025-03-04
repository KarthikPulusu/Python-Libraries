import pandas as pd
data = {
    'Name': ['Dodagatta Nihar', 'Vignesh', 'Maheshwar', 'Naman', 'Naveen', 'Shreya', 'Varsha', 'Varun'],
    'Role': ['Founder', 'Growth Manager', 'Community Manager', 'Community Manager', 'Community Manager',
             'Course Designer', 'Course Designer', 'Public Relations Manager'],
    'Phone Number': ['111-111-1111', '222-222-2222', '333-333-3333', '444-444-4444',
                     '555-555-5555', '666-666-6666', '777-777-7777', '888-888-8888'],
    'Email': ['nihar@masscoders.tech', 'vignesh@masscoders.tech', 'maheshwar@masscoders.tech', 'naman@masscoders.tech',
              'naveen@masscoders.tech', 'shreya@masscoders.tech', 'varsha@masscoders.tech', 'varun@masscoders.tech'],
    'Address': ['123, MG Road, Bangalore', '456, Brigade Road, Chennai', '789, Rajaji Nagar, Mumbai', '101, Indira Nagar, Delhi',
                '202, Koramangala, Hyderabad', '303, JP Nagar, Kolkata', '404, Electronic City, Pune', '505, HSR Layout, Ahmedabad'],
    'Blood Group': ['A+', 'B-', 'O+', 'AB+', 'A-', 'B+', 'O-', 'AB-']
}
coding_df=pd.DataFrame(data)
print(coding_df.head())
print("Description is:\n",coding_df.describe())

print("\n\nMerging data:")
roles_data={
    'Name': ['Dodagatta Nihar', 'Vignesh', 'Maheshwar', 'Naman', 'Naveen', 'Shreya', 'Varsha', 'Varun'],
    'Role': ['Founder', 'Growth Manager', 'Community Manager', 'Community Manager', 'Community Manager',
             'Course Designer', 'Course Designer', 'Public Relations Manager']
}
roles_df=pd.DataFrame(roles_data)
contact_data = {
    'Name': ['Dodagatta Nihar', 'Vignesh', 'Maheshwar', 'Naman', 'Naveen', 'Shreya', 'Varsha', 'Varun'],
    'Phone Number': ['111-111-1111', '222-222-2222', '333-333-3333', '444-444-4444',
                     '555-555-5555', '666-666-6666', '777-777-7777', '888-888-8888'],
    'Email': ['nihar@masscoders.tech', 'vignesh@masscoders.tech', 'maheshwar@masscoders.tech', 'naman@masscoders.tech',
               'naveen@masscoders.tech', 'shreya@masscoders.tech', 'varsha@masscoders.tech', 'varun@masscoders.tech']
}
contact_df=pd.DataFrame(contact_data)
merged_df=pd.merge(roles_df,contact_df,on='Name')
print(merged_df.head())




