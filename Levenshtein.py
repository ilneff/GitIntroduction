
def Edit_Distance(word_1, word_2):
	i = 0
	j = 0
	Edit_Distance_Matrix = []
	while i < len(word_1) + 1:
		Edit_Distance_Matrix.append([i])
		j=1
		while j < len(word_2)+1:

			if i == 0:
				Edit_Distance_Matrix[i].append(j)
			else:
				if word_1[i-1] == word_2[j-1]:
					Diag_Cost = Edit_Distance_Matrix [i-1][j-1]
				else:
					Diag_Cost = Edit_Distance_Matrix[i-1][j-1]+2
				Vert_Cost = Edit_Distance_Matrix [i-1][j]+1
				Horiz_Cost = Edit_Distance_Matrix [i][j-1]+1
				Edit_Distance_Matrix[i].append(min([Diag_Cost, Vert_Cost, Horiz_Cost]))
			j += 1
		i += 1

	return Edit_Distance_Matrix[i-1][j-1]
