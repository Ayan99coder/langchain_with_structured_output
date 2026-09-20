from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

class Review(TypedDict):
    name:Annotated[str,  "The personal name of the human who wrote this review. "
        "Extract the reviewer's name exactly as mentioned in the review. "
        "Never return the product name here."]
    summary : Annotated[str,'A brief summary of the review in urdu']
    sentiment : Annotated[Literal['good','bad','neutral'],'return sentiment of summary']
    prodcut_quality:str
    warranty:str
    brand_name:str
    pros :Annotated[Optional[list[str]],'write down the pros of this summary in the list ']
    cons :Annotated[Optional[list[str]],'write down the cons of this summary in urdu ']

structured_output = llm.with_structured_output(Review)
result = structured_output.invoke("""
The Apple iPhone 11 Pro is a premium smartphone that offers an impressive combination of performance, camera quality, elegant design, and display technology. Despite being released in 2019, it remains an interesting option for users looking for a compact and premium iPhone experience.

One of the most impressive features of the iPhone 11 Pro is its 5.8-inch Super Retina XDR OLED display. It delivers vibrant colors, deep blacks, and excellent contrast, making it enjoyable for watching videos, browsing social media, and viewing photos. Its stainless steel frame and matte glass back give the phone a premium appearance and comfortable feel.

The A13 Bionic chip provides smooth performance for everyday tasks, multitasking, photography, and many mobile games. The triple-camera system is another major highlight. Its 12MP Wide, Ultra-Wide, and Telephoto cameras offer flexibility for different photography situations. Night Mode improves low-light photos, while 4K video recording delivers detailed footage. The 12MP front camera also produces good-quality selfies and supports 4K video recording.

Battery life was a notable improvement over previous iPhone models at launch. However, because this is an older device, its current battery performance largely depends on battery health and usage history. Another limitation is the absence of 5G connectivity, and the base 64GB storage may feel restrictive for users who take many photos or record videos.

Overall, the iPhone 11 Pro offers a premium design, capable cameras, a high-quality display, and reliable performance. Its main strengths are its camera versatility, compact size, and build quality, while its age, battery condition, and lack of 5G are important considerations. For someone considering a used iPhone, the device's physical condition, battery health, and price should be carefully evaluated before purchasing.
Review by Ayan Javed
""")
print(result)