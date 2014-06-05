import csv
import sys

def printDiff(l, index):
	st = "["
	for i in range(len(l)):
		if i in index:
			st = st + "'" + '\033[1m' + str(l[i]) + '\033[0m' + "'"
		else:
			st = st + "'" + l[i] + "'"
		if i < len(l):
			st = st + " "
	st = st + "]"
	return st
	

def printList(l):
	for i in l:
		print i


file_paths = sys.argv[1:]
files = map(open, file_paths)
output = []

for f in files:
	for g in files:
		if f <> g:
			print "\n" + f.name + " VS " + g.name + "\n"
			f.seek(0)
			g.seek(0)
			tsv1 = list(csv.reader(f, delimiter="\t"))
			tsv2 = list(csv.reader(g, delimiter="\t"))
			r1 = 0
			r2 = 0
			tsv1_len = len(tsv1)
			tsv2_len = len(tsv2)
			num_diffs = 0
			snp_diffs = 0

			while r1 < tsv1_len and r2 < tsv2_len:
				t1 = tsv1[r1][1]
				t2 = tsv2[r2][1]
				if t1 == t2:
					if tsv1[r1][3] <> tsv2[r2][3]:
						print tsv1[r1][3], tsv2[r2][3]
						inserted = False
						for o in output:
							i = output.index(o)
							if t1 in o:
								if f.name not in output[i]:
									output[i].append(f.name)
								if g.name not in output[i]:
									output[i].append(g.name)
								inserted = True
						if inserted == False:
							output.append([t1, f.name, g.name])

					indexes = []
					for i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]: #The columns of the input files to be compared. Can contain the numbers 2 to 17 inclusive.
						if tsv1[r1][i] != tsv2[r2][i]:
							indexes.append(i)
					if len(indexes) > 0:
						print f.name + ": Line no " + str(r1+1)
						print g.name + ": Line no " + str(r2+1)
						print printDiff(tsv1[r1], indexes) + "\n" + printDiff(tsv2[r2], indexes) + "\n-------------------------"
						num_diffs = num_diffs + len(indexes)	
					r1 = r1 + 1
					r2 = r2 + 1
					continue;
				elif t1 < t2:
					num_diffs = num_diffs + 1
					snp_diffs = snp_diffs + 1
					print f.name + ": Line no " + str(r1+1)
					print g.name + ": Line no " + str(r2+1)
					print printDiff(tsv1[r1], [1]) + "\n" + printDiff(tsv2[r2], [1]) + "\n-------------------------"
					r1 = r1 + 1
					continue;
				elif t1 > t2:
					num_diffs = num_diffs + 1
					snp_diffs = snp_diffs + 1
					print f.name + ": Line no " + str(r1+1)
					print g.name + ": Line no " + str(r2+1)
					print printDiff(tsv1[r1], [1]) + "\n" + printDiff(tsv2[r2], [1]) + "\n-------------------------"
					r2 = r2 + 1
					continue;

for o in output:
	print  (len(o)-1)/len(files)
	if (len(o)-1)/len(files) >= 0.75:
		print o
		
print "Number of differnces: " + str(num_diffs)
print "Number of different SNPs: " + str(snp_diffs)