from flask import Flask,render_template,request,url_for

app = Flask(__name__)


threads = [
    {
        'title': "Insurance - General",
        'age': "16-19",
        'description': "Explore the importance of insurance and the types of insurance available here!",
        'post': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Cost",
        'age': "16-19",
        'description': "Understand how you can afford insurance to suit your needs here!",
        'post': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees",
        'age': "13-19",
        'description': "Find out how to pay off university fees without going into debt here!",
        'post': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet",
        'age': "13-19",
        'description': "Learn what is as well as the pros and cons of digital wallets here!",
        'post': 3,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card vs Credit Card",
        'age': "16-19",
        'description': "Explore the differences between debit card and credit card as well as its importance here!",
        'post': 4,
        'date_updated': "4 September 2024"
    },
]

posts = [
    [
    {
        'title': "Insurance - Introduction",
        'nav': "Introduction",
        'content': ["Insurance is described as a financial safety net that transfers the financial risks associated with health, disability, accidents, and death from an individual to an insurer. Insurance is not about expecting the worst but about being prepared for unexpected life events. People should not rely too heavily on government coverage like MediShield Lite as it only covers part of the expenses."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Insurance_Definition.png",
        'citation': "https://www.canarahsbclife.com/content/dam/choice/blog-inner/images/what-is-insurance-meaning-and-benefits-of-insurance.jpg",
        'page': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Key Policies",
        'nav': "Key Policies",
        'content': ["Hospitalisation Insurance: Essential for covering high hospital bills.", "Term Life Insurance: Provides financial protection for loved ones in case of death or permanent disability.", "Critical Illness Insurance: Covers severe illnesses like cancer, stroke, or heart attack.", "Cancer Insurance: Specifically covers all stages of cancer.", "Personal Accident Insurance: Covers medical expenses and injuries from accidents."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Insurance_Roadmap.png",
        'citation': "https://sgbudgetbabe.com/insurance-roadmap-for-gen-z/",
        'page': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Tips",
        'nav': "Tips",
        'content': ["Starting Early: The earlier you purchase insurance, the cheaper and more comprehensive your coverage can be.", "Customised Approach: Each person's needs may vary, you should adjust your insurance plans according to your circumstances.", "Change as You Grow: You can still add more coverage as you grow older and have more money to spare."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Insurance_Tips.png",
        'citation': "https://life.futuregenerali.in/media/u21mqivm/insurance-tips.jpg",
        'page': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Lecture",
        'nav': "Lecture",
        'content': ["https://www.youtube.com/watch?v=YPpdpjZ5yEw&t=39s"],
        'link': False,
        'iframe': True,
        'image_show': False,
        'video': "https://www.youtube.com/embed/YPpdpjZ5yEw?si=Tr8DU9EkI9cyy16N",
        'page': 3,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Extra",
        'nav': "Extra",
        'content': ["Links for further study"],
        'link': True,
        'links': [
                    ("https://sgbudgetbabe.com/insurance-roadmap-for-gen-z/", "Article About Insurance Roadmap"),
                    ("https://www.prudential.com.sg/wedo/wedohub/do-health/can-young-adults-even-afford-insurance-nowadays", "Article about Insurance Affordability")
                ],
        'iframe': False,
        'image_show': False,
        'page': 4,
        'date_updated': "4 September 2024"
    }
    ],
    [
    {
        'title': "Insurance - Introduction",
        'nav': "Introduction",
        'content': ["After essential expenses like CPF deductions, student loan payments, and contributions to parents, many find it challenging to allocate funds for additional expenses, such as health insurance."],
        'link': False,
        'image': "../static/images/Insurance_Definition.png",
        'citation': "https://www.canarahsbclife.com/content/dam/choice/blog-inner/images/what-is-insurance-meaning-and-benefits-of-insurance.jpg",
        'iframe': False,
        'image_show': True,
        'page': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Affordability",
        'nav': "Affordability",
        'content': ["For some, insurance is affordable even for a fresh graduate by finding a reliable insurance agent who can tailor a plan to fit an individual's budget.", "However, there are also some people who might struggle to afford both basic necessities and insurance due to various factors like pre-existing conditions and very low salaries."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Insurance_Affordability.png",
        'citation': "https://c8.alamy.com/comp/2R5P8BH/affordability-affordable-cash-icon-simple-vector-illustration-for-web-print-files-graphic-or-commercial-purposes-2R5P8BH.jpg",
        'page': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Tips",
        'nav': "Tips",
        'content': ["Early Coverage: It is important to secure health insurance early, before any health issues arise, to avoid higher premiums or exclusion due to pre-existing conditions", "Tailored Financial Planning: You should seek out insurance plans tailored to your specific financial situation, and not feel pressured to compare your financial decisions to others.", "Change as You Grow: You can still add more coverage as you grow older and have more money to spare."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Insurance_Tips.png",
        'citation': "https://life.futuregenerali.in/media/u21mqivm/insurance-tips.jpg",
        'page': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Insurance - Extra",
        'nav': "Extra",
        'content': ["Links for further study"],
        'link': True,
        'links': [
                    ("https://sgbudgetbabe.com/insurance-roadmap-for-gen-z/", "Article About Insurance Roadmap"),
                    ("https://www.prudential.com.sg/wedo/wedohub/do-health/can-young-adults-even-afford-insurance-nowadays", "Article About Insurance Affordability")
                ],
        'iframe': False,
        'image_show': False,
        'page': 3,
        'date_updated': "4 September 2024"
    }
    ],
    [
    {
        'title': "School Fees - Introduction",
        'nav': "Introduction",
        'content': ["There is a high cost of living in Singapore, exacerbated by factors like inflation, housing prices, and educational expenses. These challenges are particularly daunting for students and their families. University fees typically cost more than $8000 a year, which is not easy for normal families to pay off."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/School_Fee.png",
        'citation': "https://mtu.edu.ng/storage/news/cover/1694221586-1662132533-school-fee.jpg",
        'page': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Budgeting",
        'nav': "Budgeting",
        'content': ["Track expenses to identify unnecessary spending.", "Set a budget that prioritizes essential expenses such as tuition, rent, and groceries.", "Use budgeting apps like Seedly or Money Lover to manage finances efficiently."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Budgeting.png",
        'citation': "https://img.freepik.com/free-vector/budgeting-concept-idea-financial-planning-wellbeing-currency-balance-income-money-allocation-isolated-flat-illustration-vector_613284-1084.jpg",
        'page': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Financial Aid",
        'nav': "Financial Aid",
        'content': ["Apply for scholarships, grants, and bursaries from educational institutions, government agencies, and private organizations to reduce tuition costs.", "Consider student loans as a last resort, ensuring a thorough understanding of interest rates and repayment terms.", "Explore government schemes like the Edusave Scheme, Post-Secondary Education Account (PSEA), and SkillsFuture Credit.", "Apply for financial assistance through schemes like the MOE Financial Assistance Scheme (FAS) or the CDC/CCC ComCare Student Care Fund."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Financial_Aid.png",
        'citation': "https://inclubmagazine.com/wp-content/uploads/2024/03/Financial-Aid-decision.jpeg",
        'page': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Part-Time Employment",
        'nav': "Part-Time Employment",
        'content': ["Look for flexible part-time jobs that allow students to balance work and studies.", "Utilise university resources such as career services to find job opportunities.", "Focus on jobs that help develop transferable skills for future career prospects."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Part_Time_Employment.png",
        'citation': "https://resources.workable.com/wp-content/uploads/2017/12/shutterstock_444087613.jpg",
        'page': 3,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Frugal Living",
        'nav': "Frugal Living",
        'content': ["Take advantage of student discounts.", "Save money by cooking at home and sharing accommodation costs with roommates.", "Use student concession cards for public transportation.", "Access library resources to reduce the cost of textbooks and study materials."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Frugal_Living.png",
        'citation': "https://cdn.kobo.com/book-images/45a0f3c4-f78f-4460-8320-73651ece9930/1200/1200/False/frugal-living-your-guide-to-save-money-spend-less-and-live-better.jpg",
        'page': 4,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Financial Literacy Education",
        'nav': "Financial Literacy Education",
        'content': ["Attend workshops and seminars on financial literacy.", "Seek advice from financial professionals for personalised guidance.", "Utilise financial counselling services provided by universities.", "Reach out to community organisations for financial assistance programs."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Financial_Literacy.png",
        'citation': "https://static.vecteezy.com/system/resources/thumbnails/006/921/796/small_2x/financial-literacy-concept-free-vector.jpg",
        'page': 5,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Long-Term Financial Mindset",
        'nav': "Long-Term Financial Mindset",
        'content': ["Plan for the future by setting savings goals, investment strategies, and retirement planning.", "Build an emergency fund to cover unexpected expenses."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Financial_Mindset.png",
        'citation': "https://media.licdn.com/dms/image/v2/D4D12AQGzQJ2geilUHg/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1684233343830?e=2147483647&v=beta&t=SaGqMvDQnlIMsKR-TUSNproR5NpOQ7_NDzJdTOwoz0g",
        'page': 6,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Lecture",
        'nav': "Lecture",
        'content': ["https://www.youtube.com/watch?v=MXCvtC0HqLE"],
        'link': False,
        'iframe': True,
        'image_show': False,
        'video': "https://www.youtube.com/embed/MXCvtC0HqLE?si=Wi4P2eqaBhztHwyS",
        'page': 7,
        'date_updated': "4 September 2024"
    },
    {
        'title': "School Fees - Extra",
        'nav': "Extra",
        'content': ["Links for further study"],
        'link': True,
        'links': [
                    ("https://blog.scholarshipguide.com.sg/navigating-the-rising-cost-crisis-practical-solutions-for-students-in-singapore/", "Article About Practical Solutions for School Fees"),
                    ("https://www.youtube.com/watch?v=Xwq1KmmHN9o", "Another Video on Saving Money")
                ],
        'iframe': False,
        'image_show': False,
        'page': 8,
        'date_updated': "4 September 2024"
    }
    ],
    [
    {
        'title': "Digital Wallet - Introduction",
        'nav': "Introduction",
        'content': ["A digital wallet, also known as an electronic wallet, is a software-based system or application that stores payment information, passwords, and various other types of data (e.g., loyalty cards, event tickets, IDs) on connected devices like smartphones or computers. Digital wallets enable users to make transactions without carrying physical cards, as the payment information is stored securely within the device."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Digital_Wallet.png",
        'citation': "https://youtapinsights.com/wp-content/uploads/2022/10/digitalwallet-e1667175316583.jpg",
        'page': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet - Examples",
        'nav': "Examples",
        'content': ["Apple Pay, Google Wallet, Samsung Wallet, PayPal, Venmo, and others. Each digital wallet may offer unique features or integrations, such as Google's ability to add funds directly to the wallet or Apple's partnership with Goldman Sachs for Apple credit cards."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Digital_Wallet_Examples.png",
        'citation': "https://www.appschopper.com/blog/wp-content/uploads/2020/04/types-of-digital-wallet-appschopper1.png",
        'page': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet - Benefits",
        'nav': "Benefits",
        'content': ["Enhances security by limiting exposure to financial and personal information.", "Eliminates the need to carry physical wallets or cards.", "Increases access to financial services, especially in underserved areas."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Digital_Wallet_Pros_Cons.png",
        'citation': "https://www.narolainfotech.com/wp-content/uploads/2023/04/1-Pros-and-Cons-of-Digital-Wallets.jpg",
        'page': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet - Disadvantages",
        'nav': "Disadvantages",
        'content': ["Not universally accepted, particularly in smaller or less developed areas.", "Dependent on the availability of Bluetooth, Wi-Fi, or NFC.", "Vulnerable to identity theft or fraud if the device is stolen or hacked."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Digital_Wallet_Pros_Cons.png",
        'citation': "https://www.narolainfotech.com/wp-content/uploads/2023/04/1-Pros-and-Cons-of-Digital-Wallets.jpg",
        'page': 3,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet - Lecture",
        'nav': "Lecture",
        'content': ["https://www.youtube.com/watch?v=S_Im0Yrltkk&t=16s"],
        'link': False,
        'iframe': True,
        'image_show': False,
        'video': "https://www.youtube.com/embed/S_Im0Yrltkk?si=yms69wYVLszi2z2T",
        'page': 4,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Digital Wallet - Extra",
        'nav': "Extra",
        'content': ["Links for further study"],
        'link': True,
        'links': [
                ("https://www.investopedia.com/terms/d/digital-wallet.asp", "Article About Digital Wallet")
                ],
        'iframe': False,
        'image_show': False,
        'page': 5,
        'date_updated': "4 September 2024"
    }
    ],
    [
    {
        'title': "Debit Card and Credit Card - Introduction",
        'nav': "Introduction",
        'content': ["Debit Cards: Linked directly to a user’s bank account, debit cards allow users to spend only what they have. Transactions are immediately or shortly deducted from the linked account.", "Credit Cards: These offer a line of credit that users can borrow against, with the option to pay back later. Credit cards come with the potential to incur interest charges if balances aren't paid within the grace period."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Debit_Credit.png",
        'citation': "https://d31bgfoj87qaaj.cloudfront.net/blog/wp-content/uploads/2023/04/Credit-Cards-vs.-Debit-Cards-.jpg",
        'page': 0,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card and Credit Card - Differences",
        'nav': "Differences",
        'content': ["Impact on Credit Score: Credit cards can help build or damage your credit score, depending on usage, while debit cards do not affect credit scores since they aren't reported to credit bureaus.", "Interest Charges: Debit cards do not charge interest because they do not involve borrowing money. Credit cards, however, charge interest on outstanding balances not paid off within the grace period.", "Rewards Programs: Credit cards often offer rewards like cash back or airline miles. While some debit cards offer rewards, they tend to be less generous.", "Consumer Protections: Credit cards typically offer better consumer protection, such as limiting liability for fraudulent charges, which is generally more favourable than the protection offered by debit cards."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Debit_Credit_Diff.png",
        'citation': "https://www.investopedia.com/thmb/8-m9KcSGPVsrHMPd_sIaBe66gLM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash-050214-credit-vs-debit-cards-which-better-v2-02f37e6f74944e5689f9aa7c1468b62b.jpg",
        'page': 1,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card and Credit Card - Advantages",
        'nav': "Advantages",
        'content': ["Debit Cards: Ideal for budget-conscious users who want to avoid debt, as they limit spending to the available balance in the account.", "Credit Cards: Useful for building credit history, managing large purchases, or handling financial emergencies, provided they are used responsibly to avoid debt.", "Other Types of Cards:", "ATM Cards: These are debit cards specifically designed for withdrawing cash from ATMs and cannot be used for purchases.", "Prepaid Debit Cards: These cards are pre-loaded with a specific amount of money and can be reloaded. They are not linked to a bank account."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Debit_Credit_Diff.png",
        'citation': "https://www.investopedia.com/thmb/8-m9KcSGPVsrHMPd_sIaBe66gLM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash-050214-credit-vs-debit-cards-which-better-v2-02f37e6f74944e5689f9aa7c1468b62b.jpg",
        'page': 2,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card and Credit Card - Tips",
        'nav': "Tips",
        'content': ["Financial Management: Debit cards are more suitable for those who want to avoid debt and stick to a budget, while credit cards offer more flexibility but require careful management to avoid high-interest debt.", "Credit Building: Credit cards are crucial for building a credit history, which is important for future financial opportunities like loans or mortgages.", "Consumer Protection: Credit cards generally offer stronger protections against fraud, making them safer for online or large purchases."],
        'link': False,
        'iframe': False,
        'image_show': True,
        'image': "../static/images/Debit_Credit_Tips.png",
        'citation': "https://pikalabs.org/wp-content/uploads/2023/09/10-Tips-to-use-Pika-Labs.jpg",
        'page': 3,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card and Credit Card - Lecture",
        'nav': "Lecture",
        'content': ["https://www.youtube.com/watch?v=sm0FzHMInig"],
        'link': False,
        'iframe': True,
        'image_show': False,
        'video': "https://www.youtube.com/embed/sm0FzHMInig?si=oEK9WaSRns7yMMoT",
        'page': 4,
        'date_updated': "4 September 2024"
    },
    {
        'title': "Debit Card and Credit Card - Extra",
        'nav': "Extra",
        'content': ["Links for further study"],
        'link': True,
        'links': [
                ("https://www.investopedia.com/ask/answers/050415/what-are-differences-between-debit-cards-and-credit-cards.asp", "Article About Debit Card vs Credit Card")
                ],
        'iframe': False,
        'image_show': False,
        'page': 5,
        'date_updated': "4 September 2024"
    }
    ]
]

@app.route("/quiz_home")
def quiz():
    return render_template('quiz_home.html')

@app.route('/content')
def content():
    return render_template('content.html', threads=threads)

@app.route('/post')
def post():
    req = request.args.get('number')
    req = int(req)
    return render_template('post.html', posts=posts[req])


@app.route('/')
@app.route('/home')
def homne():
    return render_template('homepg.html')


if __name__ == '__main__':
    app.run(debug=True)
