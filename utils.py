def generate_content(task, tone, length):

    if "social media post" in task.lower():

        return f"""
{task}

Tone: {tone}
Length: {length}

Electric vehicles are driving the future of sustainable transportation. 
With lower emissions, reduced fuel costs, and advanced technology, EVs are becoming a smarter and greener choice for modern mobility.
"""

    elif "blog" in task.lower():

        return f"""
Blog Topic: {task}

Tone: {tone}
Length: {length}

Artificial Intelligence is transforming modern industries rapidly. 
From hiring and healthcare to automation and customer support, AI helps businesses improve efficiency and decision-making.
"""

    elif "email" in task.lower():

        return f"""
Subject: Job Application

Dear Hiring Manager,

I hope you are doing well. I am writing to express my interest in the position. 
Please find my application attached for your review.

Thank you for your time and consideration.

Best Regards
"""

    else:

        return f"""
Task: {task}

Tone: {tone}
Length: {length}

Generated content successfully.
"""