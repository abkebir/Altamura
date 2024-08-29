import streamlit as st

# Page configuration
st.set_page_config(page_title="Migr-Action Final Event", layout="wide")

# Main title of the page
st.title("Migr-Action Final Event")

# Brief description of the event
st.write("""
Join us for the culminating event of Migr-Action, a dynamic and immersive experience celebrating youth voices and stories of migration.
Explore creative work from 27 young participants across Italy, France, Germany and Tunisia as they delve into the complexities of migration through various mediums.


**Location:**
Altamura, Santa Croce

**Date:**
August 30, 2024

**Time:**
07:00 - 08:30 PM

Use the sidebar to navigate through the different stories of the event.
""")


# Barre latérale avec un menu de navigation
section = st.sidebar.selectbox(
    "Naviguer entre les sections",
    ["Introduction", "Section 1", "Section 2", "Section 3", "Section 4", "Section 5", "Section 6"]
)

# Affichage du contenu en fonction de la section sélectionnée
if section == "Introduction":
    st.header("Introduction")
    st.write("""
Through various mediums, these participants will showcase their unique perspectives on one of the most pressing issues of our time. From immersive audio installations to intimate performances and interactive exhibitions, this event offers a multifaceted experience that highlights the diversity and complexity of migration stories.

Set against the historic backdrop of Santa Croce in Altamura, Italy, this event provides a powerful platform for dialogue and cultural exchange. Attendees will have the opportunity to witness the creativity and resilience of these young voices as they navigate and express their migration narratives. 

Don’t miss this extraordinary event that bridges cultures and connects communities through art and storytelling.    """)

elif section == "Section 1":
    st.header("Section 1: A story from Tunisia")
    st.write("""
    While the personal stories of migration bring the detrimental aspects of migration on the
migrants and its impacts on his life and the lives of those around him.
Migration in folklore tells the history of a whole nation, a story of perseverance and
determination.
And as a Tunisian,no story of migration will ever retell our history more than that of Alyssa
(also known as Dido). She was a Phoenician princess to Tyre (modern Lebanon) in 800 Bc ,
married to a wealthy man and lived as happy as one can be.
As the days passed, her older brother pygmalion, the heir to the throne, wanted her
husband's wealth and ended up killing him to get his money. Fearing for her own life, Alyssa
fled in the dead of night with a few of her loyal servants to escape her brother and sailed on
the Mediterranean Sea.
As days passed, she found herself on a land that reminded her of home, a land where she
wanted to settle and build a new life. This task seemed quite impossible with the refusal of
the chief of the town, as no foreigner could own land. She begged and pleaded, and as a
last resort, desperately asked for land even as big as a bull's skin. A plea so outrageously
bizarre that the chief could not but accept.
But Alyssa was known for being quite determined and extremely cunning. She cut the bull's
hide into thin strips to create a decent piece of land that she managed to negotiate and build
a castle on the hill. Her intelligence and iron will got her to be a welcomed member in the city
that she later named Carthage, meaning "New City," referencing her homeland.
Close by, a Trojan prince fled his war-riddled country alongside his son after his wife's death
and sought refuge in Carthage, asking for money and soldiers. During his stay, he managed
to capture Alyssa's interest, and she asked him to stay in Carthage and build a new life with
her.
But he refused, he had too many obligations towards his people and his soldiers that he
could not just abandon them. This absolutely enraged Alyssa that she went as far as to
kidnap his son in a desperate attempt to get him to stay. An attempt that soon seemed
useless as everyone berated her.
As the guilt kept slowly eating her alive, she gave the boy back and organized a big farewell
party for the prince with food, a big barbecue, and all the festivities. Later in the evening, as
the flames kept on igniting and the prince packed his things to go, Alyssa made one last
speech. She apologized for what she had done, the pain she had caused, and how she
tainted her late husband's memory, and then threw herself into the flames.

    """)
    st.image("./images/pitcur1.jpeg", caption="Description de l'image 1")

elif section == "Section 2":
    st.header("Section 2: A story from Tunisia")
    st.write("""
I am a Palestinian student from Gaza studying at the Faculty of Medicine in Sousse. My story began when I succeeded in the baccalaureate with a very high average. I wished to study medicine in my country alongside my family, but my grades didn't qualify me for universities in Gaza. The difference was minimal, but I started studying pharmacy and was content with that choice. However, when scholarships became available on the ministry's website, the first was from Morocco, but I couldn't register because the deadline had passed. Then came a scholarship from Algeria, but my name wasn't among the candidates. I felt hopeless and decided to continue my studies in my country and specialization. However, when a scholarship to Tunisia became available, my elder brother didn't want me to lose hope. He was more eager than me to register, However, I told him I definitely didn't want it, but without my knowledge, my brother entered my information and registered on my behalf. After some time, I received an acceptance letter, and he came to inform me, which was a pleasant surprise as I had no idea. It was truly a strange twist of fate, and I started preparing for the journey. However, the journey was extremely exhausting because we had to travel through the Palestinian-Egyptian land route. Initially, it was tough for us to pass through these borders, and after numerous exhausting attempts, we finally managed to reach Tunisian territory.
Initially, it was challenging to adapt to Tunisia due to cultural differences, dialects, interactions, and even the language of instruction. 
However, my fear quickly dissipated when l received a warm reception from the locals upon learning we were from Palestine. This created a sense of comfort for me and we began learning the dialect, cuisine, and social norms. Many aspects made the beginning both wonderful and difficult at the same time.
Afterwards, me and others palistinains girls settled in Sousse and began adjusting to life anew, starting my studies at the Faculty of Medicine. 
Initially, I felt a strange sensation seeing all the students together, quickly getting to know each other, most of whom already knew each other. It felt like a period of isolation 
I experienced two phases of adaptation, not just one. Afterward, I decided to get to know people and integrate into the community and among the students. 
I began to gradually meet students from my group until I knew a large number of them. That was when I found happiness. I felt part of the college, seeing people I knew and had good relationships with, exchanging greetings with each other. I felt closeness at that time, feeling I belonged to this community, not a stranger. I found them helping me with my studies because it was a completely new and difficult language at first, but I quickly adapted to the reality. From there, I began my journey of discovery in Tunisia. I visited many tourist attractions and tried to learn about as many cultures as possible. I still continue to discover and love experiencing everything new.
    """)
    st.image("./images/picture2.jpeg", caption="Description de l'image 2")

elif section == "Section 3":
    st.header("Section 3: A story from Italy")
    st.write("""
An incredible story of an international student in Italy

My life is like a roller coaster traveling from city to city to study and work. I was born into a middle class family and have one brother. 
I have studied all my life with scholarships or government funded money. I was much more worried about my father. 
In 2022 when I was working in the IT industry as an accountant. I'm doing research to move abroad and I also want to do my master's degree. 
After doing some research I discovered that Italy is the perfect choice because it is located in the center of Europe. I was selected at the University of Naples for the International Relations program. This program also offers scholarship opportunities. But unfortunately I don't get scholarship money in my first year.
Only then do I realize how out of my comfort zone life is. I stood in the streets nearby begging like I missed the last train after work and a lot of messed up experience, but Naples never let me down. I build good contacts, good networks with many new international friends. Wow, that's an amazing journey I've been on in my entire life.
Finally right now I'm almost finishing my master's degree. In the end if you’re dream is big and if want someting dont wait it will automatically come to you go for it and make it on your own and please don't break down when you have the worst days of your life. There are lot of opportunities around us everytime. Thank you !
    """)
    st.image("./images/picture3.jpeg", caption="Description de l'image 3")

elif section == "Section 4":
    st.header("Section 4: A story from Germany")
    st.write("""
At night, the light stays on.

A Berlin woman is hosting in Ukrainian refugees. Along with the family came the horrors of war.

The little girl runs back and forth. She throws herself against the bars of the crib where her brother is standing. Then she runs back to her mother, who takes her on her lap and looks out of the window. Present, but somehow not. The woman and her family have lived here in the old Berlin apartment since March 5, 2022. They fled Ukraine in four generations: grandchildren Daniel and Rosa (1 and 2), daughter Daria (22), mother Ekaterina (58) and grandmother Nadia (77). Now they are sitting at the table with tea and biscuits at lunchtime with Friederike, who has taken them in. They all want to only publish their first names. What the family has experienced is too close to their hearts, and Friederike is not keen to be in the public eye, she simply wants to help. 
Before leaving the city of Kiev, the family had held out in a cellar for six days. That is what the young mother Daria tells me - or rather, what her smartphone tells me. She has opened a translation program and is typing eagerly. 
Then a monotone voice comes out of the speaker and continues to tell of the atrocities: "After a week, the children could no longer bear it. They cried a lot and were afraid of explosions." None of the women speak English. When Ekaterina says something, she speaks slowly in Ukrainian, gesticulating with her hands and feet. Daria sits quietly and types into her phone. This is how they have been communicating with Friederike for weeks now. Ekaterina shows her escape route on the screen of her phone. They have taken the train via Lviv to a Polish border town. The 58-year-old stretches her palms forward to show how they were pushed into the carriages. From there, they travelled to Berlin on a bus organized by volunteers. 20 hours. Some of the refugees slept so deeply in their seats that the volunteers began to take their pulse - fearing that they might have died on the journey. Friederike's daughter is also a volunteer at the central bus station and is in contact with the initiator who organized the trip for a total of 170 refugees in three buses. She is the one who called her mother and put the family in touch with her. Friederike agreed immediately to host them. "I can't help the people from Ukraine financially, but I have living space that I can make available." 
The family lives in the room of Friederike's daughter, who moved out a year ago, while her son still lives in the apartment with his mother and the new guests.
The books on the shelves now help the children to pass the time - and Ekaterina to learn German. She points to the desk. Next to " Raupe Nimmersatt" is a handwritten note with Cyrillic letters. She is practicing the numbers. One cat, two socks, ten dogs. The family lives in two bright rooms. Floorboards creak under the colourful carpet, beds are everywhere, suitcases and plastic bags lie around. The air is thick. 
Every now and then they eat together. "Ekaterina is the kitchen chef. She often goes to the market and cooks borscht or blini for everyone," says Friederike. "She wants to clean to distract herself. I understand that." But there are also moments that bear witness to what this family has been through in recent weeks. "They leave the room light on at night. They're scared when the garbage collectors come, and garbage cans are pushed across the asphalt." Friederike closes daily newspapers that show pictures of the destroyed Ukrainian capital. 
When her son watches action movies, he puts on headphones.
Due to the language barrier, communication focuses on organizational matters; she only gets insights into their emotional world non-verbally, says Friederike. She doesn't dare ask such questions via a translator app, questions about the time in the cellar, the flight or the situation of Daria and Ekaterina's husbands in Kiev.
    """)
    st.image("./images/picture4.jpeg", caption="Description de l'image 4")

elif section == "Section 5":
    st.header("Section 5: A story from Germany")
    st.write("""
An unpolitical city.

Today is a big day. Months of eager board discussions, secret-keeping and impatient anticipation. Even though Spring is not yet around the corner, the city feels like it is waking up. Carnival is beginning, bringing six weeks of happy celebration, lots of alcohol and costuming with it. People like to call it the fifth season, and it starts tonight, with the season-opening carnival show, promising more or less humorous speeches, themed dances performed and the reveal of the new seasonal and somewhat-serious prince and princess. 
Being picked for this position is a high honour he thinks, reminiscing the sweet memories of the carnival season where he got to fill this position 28 years ago. In the past years he got to pick the new couple. The occurrence of any romantic feelings prevented by the prince being at least a quarter century older, the couple is nominated freshly every year, on the basis of involvement in previous carnival seasons, connections with important carnival club members and financial fluidity. 
Carnival is great fun, yet there are also a lot of rules. Those rules, he believes, keep the magic of the celebration and prevent unpleasant surprises. He will never forget the catastrophic speech of a young woman last year. It felt like mockery, her humorously pointing out what she thinks of those rules and traditions, they all work so hard for to keep up. She might have a point, that it is weird that the reigning couple always has to consist of a younger woman and an older man or that the stage council is made up only of men. Even though he did not get her point of cultural appropriation, when talking about China- or India-themed dances. After all, they are nice to look at and just for fun. She was politicizing an unpolitical event and he had felt a little uncomfortable. His association is open towards everyone, even migrants. And he does not want to see colour, wouldn’t that be racist? The Turkish, Polish and migrant community of his home town simply has no interest in taking part in those celebrations. Their loss. It is just great fun. And she was confronting them with absurd accusations. Subtly shaking his head, thinking of this memory, he thought: No, you should be able to say everything. Carnival is supposed to be fun. Not political. At least not too much. They should stick to making fun of the mayors new blonde hair colour, laughing about the lengthy remodelling of the local one-track train station or mocking the hardships of being married to talkative wifes. 
His wife had prepared his evening suit and large traditional hat,  somehow shaped like a very narrow white boat. He gets to wear this being a member of the associations planning board, which always makes him stand a little taller. Just one last glance through the local newspaper. Turning the pages past the weather report, news from the upcoming district football tournament and the renovation of the city hall, he finds an article about a new research on secret so called “remigration”-plans, made by various members of the AfD and other known right-wing leaders. Their goal to remove people with any migration background from Germany has first been reported about a few days ago, and since then caused a lot of demonstrations. He fervently hopes those news will not be picked up tonight. You never know if one of the 25% percent of AfD-voters are part of tonights audience. They would feel lectured and repelled, which is not what he wants. Carnival is for everyone. It is inclusive. It is not political. 
    """)
    st.image("./images/picture5.jpeg", caption="Description de l'image 5")

elif section == "Section 6":
    st.header("Audios section")
    st.write("""
    Résumé de l'histoire 6. Cette histoire illustre...
    """)
    st.audio("./audios/AUD-20240724-WA0008.mp3")  # Ajout du fichier audio avec un bouton Play

    st.audio("./audios/At Night, the Light stays on.mp3")  # Ajout du fichier audio avec un bouton Play
    
# Footer ou espace additionnel si besoin
def display_footer():
    st.write("---")
# "Participants" section
    st.write("### Participants")

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        st.image("./flags/logo link _bianco 2.jpg", caption="Italy", width=220)

    with col4:
        st.image("./flags/Logo_Diagonal.jpeg", caption="France", width=130)


    with col5:
        st.image("./flags/GESW-Logo.jpeg", caption="Germany", width=170)

    with col6:
        st.image("./flags/logo_atacjl.jpeg", caption="Tunisia", width=170)

    


    # "Supported by" section
    st.write("### Supported by")
    
    col1, col2 = st.columns([1, 1])  # Equal width for both columns
    with col1:
        st.image("./flags/EU_POS.jpeg", caption="European Union", width=170)
        
    with col2:
        st.image("./flags/LOGO_OFAJ_CARTOUCHE_RVB_BLEU.jpeg", caption="Franco-German Youth Office", width=120)

    
    # Contact Information
    st.write("For more information, contact: +39 3278393352")

# Call the footer function to display it on all pages
display_footer()
