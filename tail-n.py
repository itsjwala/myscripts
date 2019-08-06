import time
import os
import sys

def tail(f, n):
	assert n >= 0
	pos, lines = n+1, []

	# set file pointer to end

	f.seek(0, os.SEEK_END)

	isFileSmall = False

	while len(lines) <= n:
		try:
			f.seek(f.tell() - pos, os.SEEK_SET)
		except ValueError as e:
			# lines greater than file seeking size
			# seek to start
			f.seek(0,os.SEEK_SET)
			isFileSmall = True
		except IOError:
			print("Some problem reading/seeking the file")
			sys.exit(-1)
		finally:
			lines = f.readlines()
			if isFileSmall:
				break

		pos *= 2

	for line in lines[-n:]:
		print(line,end="")
	print()


if __name__ == "__main__":
	doFollow = False
	val = sys.argv[1]
	if val[0] == 'f' or val[0] == 'F':
		doFollow = True
		n = int(val[1:])
	elif val[-1] == 'f' or val[-1] == 'F':
		doFollow = True
		n = int(val[:-1])
	else:
		n = int(val)


	filename = sys.argv[2]


	with open(filename) as f:

		if doFollow:

			while(True):
				time.sleep(0.3)
				tail(f,n)
		else:
			tail(f,n)
