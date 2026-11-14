class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        cnt = 0
        u = set()

        for email in emails:

            label, domain = email.split("@")

            label = label.split("+")[0]
            label = "".join(label.split("."))

            final_email = label+"@"+domain
            
            if final_email not in u:
                u.add(final_email)
                cnt += 1
        
        return cnt


        
