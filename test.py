from gtts import gTTS
import csv

def splitJp(example):
	exampleArr = example.split('/')
	jpExample = []
	for index, row in enumerate(exampleArr):
		if row:
			jpExample.append(row)
	
	return jpExample

def getNo(level, lineNo):
	if int(level) == 2:
		lineNo = int(lineNo) - 101
		return str(lineNo)
	elif int(level) == 3:
		lineNo = int(lineNo) - 282
		return str(lineNo)
	elif int(level) == 4:
		lineNo = int(lineNo) - 417
		return str(lineNo)
	elif int(level) == 5:
		lineNo = int(lineNo) - 466
		return str(lineNo)
	else:
	  	return lineNo

def saveJpAudio(level, lineNo, pattern, jpExample):
	No = getNo(level, lineNo)

	tts = gTTS(pattern, lang = 'ja')
	tts.save(f'build/tts/jp/pattern/{lineNo}.mp3')

	for index, row in enumerate(jpExample):
		tts = gTTS(row, lang = 'ja')
		tts.save(f'build/tts/jp/N{level}-{No}-{index+1}.mp3')

with open('JLPT bunpou - tts output.csv') as csvfile:
	reader = csv.reader(csvfile)
	for index, row in enumerate(reader):

		if index == 0: continue
		# if index > 2: break

		jpExample = splitJp(row[3])
		print(f'{jpExample}')

		saveJpAudio(row[2],row[0], row[1], jpExample)
