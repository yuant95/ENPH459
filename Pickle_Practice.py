import pickle  # import module first
import json
# f = open('people_ALL.pkl', 'rb')  # 'r' for reading; can be omitted
# people_data = pickle.load(f,encoding='latin1')
# # using encoding='latin1' because the file was pickled in python 2, python3 was trying to unpickle everything
# # to 'str' using ascii codec, but ascii does not support
# f.close()
f = open('2016-05-18t09.35.32_capture_all.pkl', 'rb')
capture_data = pickle.load(f,encoding='latin1')
f.close()

# print(people_data)
print(capture_data)


# with open('captures_2016-05-19_to_2016-07-10.json',encoding="utf8") as json_data:
#     d = json.load(json_data)
#     print(d)

