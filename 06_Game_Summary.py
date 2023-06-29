game_summary = []

questions_answered = 0
num_wrong = 0

questions_right = questions_answered - num_wrong

percent_correct = questions_right / questions_answered * 100
percent_wrong = num_wrong / questions_answered * 100

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Correct: {} \t|\t Wrong: {} \t|\t "
      .format(questions_answered, num_wrong, ))

print("****** Game Statistics ******")
print("Correct: {}, ({:.0f}%)\nWrong: {}, "
      "({:.0f}%)\n, ".format(questions_right,
                             percent_correct,
                             num_wrong,
                             percent_wrong))

print()
print("Thanks for playing")
