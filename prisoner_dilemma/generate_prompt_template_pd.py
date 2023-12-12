
def pd_prompt(total_rounds, round_num, feature, round_history_str, player_number, payoff_matrix, your_earnings, opponent_earnings, questionaire=False):
    template = f'''
Game Instructions:
In this game, you are the player {player_number} (described below).
Your goal is to maximize your total payoff over {total_rounds} rounds.

In each round, you can select one of the two choices: cooperate or defect.
The other player will also select cooperate or defect, and the payoffs you get in each round will depend on both of your choices.

Payoff is determined as follows:
1. If both of you cooperate, then both of you get {payoff_matrix[0][0]} dollars
2. If one player cooperates and the other player defects, then the cooperating player gets {payoff_matrix[0][1]} dollars and the defecting player gets {payoff_matrix[1][0]} dollars
3. If both of you defect, then both of you get {payoff_matrix[1][1]} dollars

Please carefully read the above payoff determination rule and remember it.
Note that in each round, you and the other player make choices simultaneously.
You will be given the choices and payoffs of both players in past rounds.
Your total payoff in this game will be the cumulative sum of the payoffs you obtain over {total_rounds} rounds.
'''

    if round_num == 1:
        template += f''' Now let us begin the game!
Recall that you are the player {player_number}.
'''
    else:
        template += f'''
Recall that you are the player {player_number}.
You have played {round_num - 1} round(s) before.
Here is the history of the gameplay of previous rounds: {round_history_str};
Your total payoff so far: {your_earnings} dollars;
The other player's total payoff so far: {opponent_earnings} dollars.
'''
            
    if questionaire==False:
        template += f'''
Please provide your choice in this round by completing the following: 'I choose []'.
Replace [] with your choices.

This is round {round_num} of the game with {total_rounds - round_num} round(s) left.
Important: Please pretend that you are a human in the game with the following features when making decision: {feature}
Please answer in the exact format (no need to tell your reasoning).
'''
    else:
        template += f'''
Please provide your answer in this round in a single-line JSON format with two keys: "reasoning" and "decision"
{{"reasoning": "...", "decision": "..."}}
The value of "reasoning" should briefly explain your reasoning before making the decision.
The value of "decision" should be either "cooperate" or "defect".

This is round {round_num} of the game with {total_rounds - round_num} round(s) left.
Important: Please pretend that you are a human in the game with the following features when making the decision: {feature}
Please answer in the exact format.
'''
        
    return template