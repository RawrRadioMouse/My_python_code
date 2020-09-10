#You've updated the score of every HackerRank user who participated in a contest. Sometimes, HackerRank admins also participate in a given contest but care #is taken to ensure that their submissions do not get any score and their score is not updated.

#Like the previous challenge, you are given a method scoring with an array passed as an argument. Each element of the array is of class User.


def scoring(array)
    array.each do
        |user| user.update_score unless user.is_admin?
    end
end