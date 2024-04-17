class Email:
    """
    Represents an email with properties like email address, subject line,
    email content, and read status.
    """
    def __init__(self, email_address, subject_line, email_content):
        """
        Initialize an Email instance.

        Args:
            email_address (str): The sender's email address.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
        """
        self.email = email_address
        self.subject = subject_line
        self.content = email_content
        self.has_been_read = False

inbox = []

def populate_inbox():
    """
    Populate the inbox with predefined Email instances.
    """
    # Create Email instances and add them to the inbox list
    first_proposal = Email("fdarcy@pemberley.com", "My Proposal Despite My Reservations",
                           "Dear Miss Bennet,\nI write to express my profound admiration and "
                           "to request the honor of your hand in marriage, despite the differences "
                           "in our stations.")
    second_proposal = Email("collins@hunsford.com", "Holy Matrimony",
                            "Dear Miss Bennet,\nI write to request the honor of your hand in "
                            "marriage, considering the advantages it would afford both of us.")
    third_proposal = Email("fdarcy@pemberley.com", "You have bewitched me",
                           "Dear Miss Bennet,\nI humbly write to seek your forgiveness for "
                           "my past errors and to renew my earnest plea for your hand in marriage, "
                           "now enlightened by a deeper understanding of your worth.")
    inbox.extend([first_proposal, second_proposal, third_proposal])

populate_inbox()

def list_emails():
    """
    Display the list of emails currently in the inbox.
    """
    print("Currently in your inbox:")
    for index, email in enumerate(inbox):
        print(index + 1, str(email.subject))

def list_unread_emails():
    """
    Display the list of unread emails in the inbox and return the number of unread emails.
    """
    print("\nUnread emails in your inbox:")
    unread_count = 0
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            unread_count += 1
            print(index + 1, str(email.subject))
    if unread_count == 0:
        print("No unread emails.")
    return unread_count

list_emails()

def read_email(selected_serial):
    """
    Display the content of a selected email, mark it as read, and return the updated unread count.

    Args:
        selected_serial (int): The serial number of the email to be viewed.

    Returns:
        int: The number of unread emails after marking the selected email as read.
    """
    if 1 <= selected_serial <= len(inbox):
        selected_email = inbox[selected_serial - 1]
        print("\nFrom: ", selected_email.email, "\nSubject: ", selected_email.subject,
              "\nMessage: ", selected_email.content)
        selected_email.mark_as_read()
        print("\nRead Status:", "Read" if selected_email.has_been_read else "Unread")
    else:
        print("Invalid serial number.")
    
    return list_unread_emails()

unread_count = list_unread_emails()

while unread_count > 0:
    try:
        selected_serial = int(input("\nPlease enter the serial number of the email you want to view. Enter 0 to exit: "))
        if selected_serial == 0:
            break
        else:
            unread_count = read_email(selected_serial)
            if unread_count == 0:
                print("\nNo unread emails. Exiting...")
                break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nGoodbye!")
