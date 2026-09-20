from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field,EmailStr,field_validator
load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-3.7-flash')
class Review(BaseModel):
    name : str=Field(
        description="Person name",
         min_length=3,
        max_length=20
    )
    #custom_validator
    @field_validator('name')
    @classmethod
    def validate_username(cls, value):
    #we can use if conditions and related too
        return value.lower()
    #literal + Optional + field
    sentiment : Optional[Literal['good','bad','neutral']]= Field(description='Sentiment about summary',default=None)
    #default values + validation
    email: Optional[EmailStr] = None
    #optional + default
    phone_number : Optional[str] = None
structure_output = llm.with_structured_output(Review)
output =structure_output.invoke('''The Apple iPhone 11 Pro is a premium smartphone that offers an impressive combination of performance, camera quality, elegant design, and display technology. Despite being released in 2019, it remains an interesting option for users looking for a compact and premium iPhone experience.

One of the most impressive features of the iPhone 11 Pro is its 5.8-inch Super Retina XDR OLED display. It delivers vibrant colors, deep blacks, and excellent contrast, making it enjoyable for watching videos, browsing social media, and viewing photos. Its stainless steel frame and matte glass back give the phone a premium appearance and comfortable feel.

The A13 Bionic chip provides smooth performance for everyday tasks, multitasking, photography, and many mobile games. The triple-camera system is another major highlight. Its 12MP Wide, Ultra-Wide, and Telephoto cameras offer flexibility for different photography situations. Night Mode improves low-light photos, while 4K video recording delivers detailed footage. The 12MP front camera also produces good-quality selfies and supports 4K video recording.

Battery life was a notable improvement over previous iPhone models at launch. However, because this is an older device, its current battery performance largely depends on battery health and usage history. Another limitation is the absence of 5G connectivity, and the base 64GB storage may feel restrictive for users who take many photos or record videos.

Overall, the iPhone 11 Pro offers a premium design, capable cameras, a high-quality display, and reliable performance. Its main strengths are its camera versatility, compact size, and build quality, while its age, battery condition, and lack of 5G are important considerations. For someone considering a used iPhone, the device's physical condition, battery health, and price should be carefully evaluated before purchasing. review by Ayan Javed, email : ayanjaved803@gmail.com''')
print(output.model_dump_json())