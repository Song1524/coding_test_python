def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!

    play_dict = {}
    total_play_dict = {}

    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]

        if genre in total_play_dict:
            total_play_dict[genre] += play
            play_dict[genre].append([i, play])
        else:
            total_play_dict[genre] = play
            play_dict[genre] = [[i, play]]

    sorted_genre = sorted(total_play_dict.items(), key=lambda item: item[1], reverse=True)

    answer = []

    for genre, total_play in sorted_genre:
        sorted_play =  sorted(play_dict[genre], key=lambda item: item[1], reverse=True)

        count = 0
        for index, play in sorted_play:
            if count >= 2:
                break

            answer.append(index)
            count +=1

    return answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))