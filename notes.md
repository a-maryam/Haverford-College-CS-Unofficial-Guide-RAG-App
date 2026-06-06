First prompt

Can you use planning.md as a basis to write a script to load all the documents from docs, define a method for paragraph chunking, define a method for fixed-length chunking as per parameters in planning.md? Do the previous as functions, then make the appropriate calls to paragraph chunk and fixed-length chunk respectively as define.

Chunks:

Total chunks: 369

# Notes about reddit chunks
    Seems like there are a lot of things semantically mixed together in the reddit chunks that I printed...hopefully the paragraph split is better.

{'source': '10_reddit_cs_2.txt', 'method': 'fixed', 'chunk_index': 0, 'text': "How is the Computer Science and Math departments here?\nAre the professors good? I've heard a lot about them.\nAlone-Monk\n•\n1y ago\nI dunno much about comp sci but our Math department is really good imo\n\n\nUpvote\n4\n\nDownvote\n\nReply\n\nAheniru\n•\n1y ago\nAlum (class of '24)\nI’ve heard the math department is one of the best and CS is not the best but depends. I was a CS major (‘24) - I think BMC generally had better intro CS classes. I think ML and data science at Hav was absolutely fantastic due to the p"}


{'source': '10_reddit_cs_2.txt', 'method': 'fixed', 'chunk_index': 1, 'text': "ad better intro CS classes. I think ML and data science at Hav was absolutely fantastic due to the profs teaching it while I was there. I think it was better there than at Penn. I also appreciate how there’s not a weeding out process in CS in the bi-co but I definitely feel like the intro classes are the hardest and it gets easier from there.\n\n\n\nUpvote\n3\n\nDownvote\n\nReply\n\nseaflans\n•\n1y ago\nThe hardest is definitely Dianna Xu's Analysis of Algorithms at BMC, but it's also a great class. I think i"}


{'source': '10_reddit_cs_2.txt', 'method': 'fixed', 'chunk_index': 2, 'text': "dest is definitely Dianna Xu's Analysis of Algorithms at BMC, but it's also a great class. I think it's listed as CS340.\n\n\n\nUpvote\n2\n\nDownvote\n\nReply\n\nAheniru\n•\n1y ago\nAlum (class of '24)\nI took it with Lindell since I was not confident with being able to pass her class haha Her OS class is also very hard (I’ve heard)\n\n\n\nUpvote\n2\n\nDownvote\n\nReply\n\nseaflans\n•\n1y ago\nPretty sure analysis of algorithms with Dianna was my worst grade on my transcript, and I was quite pleased with the grade I receive"}


{'source': '10_reddit_cs_2.txt', 'method': 'fixed', 'chunk_index': 3, 'text': "ms with Dianna was my worst grade on my transcript, and I was quite pleased with the grade I received.\n\n\nUpvote\n2\n\nDownvote\n\nReply\n\nu/Kingtastic1 avatar\nKingtastic1\n•\n1y ago\nJunior (class of '28)\nThe computer science department is hit or miss. I've known two professors that are leaving after this year, and I also know students that came in being a compsci major and completely switching out because they felt like the department isn't helping them learn how to program. I've personally found it oka"}


{'source': '10_reddit_cs_2.txt', 'method': 'fixed', 'chunk_index': 4, 'text': "they felt like the department isn't helping them learn how to program. I've personally found it okay, but it is the courses I am performing the worst in academically (I am a CS major)\n\n\n\nUpvote\n2\n\nDownvote\n\nReply\n\nAheniru\n•\n1y ago\nAlum (class of '24)\nWhich profs are leaving?\n\n\n\nUpvote\n1\n\nDownvote\n\nReply\n\nu/Kingtastic1 avatar\nKingtastic1\n•\n1y ago\nJunior (class of '28)\nI'll PM you.\n\n\nUpvote\n2\n\nDownvote\n\nReply\n\nDifferentSea5841\n•\n1y ago\nWhich professors are leaving?\n\n\nUpvote\n1\n\nDownvote\n\nReply\n\nCi"}


# Lottery info chunks:
    The preamble type paragraphs don't seem to be helpful. But I think the course info is chunked together

{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 32, 'text': 'In addition to submitting the written thesis document, students must also complete the assigned presentation elements, which typically include a December poster presentation of the thesis topic and scope, and the final oral presentation of the thesis. These presentations are graded on evidence of preparation and on participation (i.e. showing up on time for one’s own presentation, attending the rehearsals of a few others, and providing feedback and/or asking questions). Faculty will provide info'}


{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 33, 'text': 'hearsals of a few others, and providing feedback and/or asking questions). Faculty will provide informal feedback to the presenters on speaking style, professionalism, diction/grammar, poise, etc., but these elements are not included in the grade.'}


{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 34, 'text': 'Minor Requirements\nThe Computer Science minor requirements follow the same philosophy and structure as the major:'}


{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 35, 'text': 'the introductory sequence\nbreadth: a 200-level course in each element of the field (theory, systems, and applications)\ndepth: one year-long sequence (200-level into 300-level) in either theory, systems, or applications\nCMSC H105 Introduction to Computer Science or CMSC H107 or Bryn Mawr CMSC B113.\nCMSC H106 Introduction to Data Structures or CMSC H107 or Bryn Mawr CMSC B151.\nCMSC H231 Discrete Mathematics\nStudents with strong backgrounds in mathematics and prior knowledge of the topics covered i'}


{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 36, 'text': 'hematics\nStudents with strong backgrounds in mathematics and prior knowledge of the topics covered in CMSC H231 may wish to seek instructor permission to place into CMSC H340 /CMSC H345 without prior completion of CMSC H231—in this case, the student may complete the requirements for the minor with another course covering discrete mathematics, from the following list: MATH H210 (Linear Optimization), MATH H394 (Logic), MATH H394 (Cryptography), MATH H395 (Combinatorics), or STAT H203, STAT H218,'}


{'source': '11_haverford_cs_reqs.txt', 'method': 'paragraph', 'chunk_index': 37, 'text': '), MATH H394 (Logic), MATH H394 (Cryptography), MATH H395 (Combinatorics), or STAT H203, STAT H218, STAT H286, or STAT H396.\nCMSC H251 Principles of Computing Systems\nStudents wishing to continue to CMSC B355 may substitute CMSC B223 Systems Programming\nStudents not taking a 35X course may substitute CMSC H240 Principles of Computer Organization or CMSC H245 Principles of Programming Languages\nCMSC H260 Foundations of Data Science\nOne 300-level core course from the following list\nCMSC H340 Analy'}
