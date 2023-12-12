

def ug_proposer_prompt(sum_of_money, total_rounds, round_num, feature, round_history_str, proposer_earnings, responder_earnings, questionaire=False):
    template = f'''
Game Instructions:
In this game, you are the proposer (described below).
Your goal is to maximize your total payoff over {total_rounds} rounds.
As the proposer, in each round, your task is to divide a sum of {sum_of_money} dollars between yourself and another player.
Subsequently, another player (a responder) will then either accept or reject your proposal.
If they accept, then the money will be divided according to your proposal. If they reject, you two will earn nothing.
You will be given the choices and payoffs of both players in past rounds.
Your total payoff in this game will be the cumulative sum of the payoffs you obtain over {total_rounds} rounds.
'''
    
    if round_num == 1:
        template += f'''
Now let us begin the game!
Recall that you are the proposer.
'''
    else:
        template += f'''
Recall that you are the proposer.
You have played {round_num - 1} round(s) before.
Here is the history of the gameplay of previous rounds: {round_history_str}.
Your total payoff so far: {proposer_earnings} dollars;
The other player's total payoff so far: {responder_earnings} dollars.
'''

    if questionaire==False:
        template += f'''
Please provide your offer in this round by completing the following: 'I keep [] dollars to myself and offer [] dollars to the other player.'
Replace [] with your choices.

Subsequently, a responder will then either accept or reject your proposal.
If they accept, then the money will be divided according to your proposal. If they reject, you two will earn nothing.
This is round {round_num} of the game with {total_rounds - round_num} round(s) left.
Important: Please pretend that you are a human in the game with the following features when making the decision: {feature}
Please answer in the exact format (no need to tell your reasoning).
'''
    else:
        template += f'''
Please provide your answer in this round in a single-line JSON format with two keys: "reasoning" and "decision"
{{"reasoning": "...", "decision": "..."}}
The value of "reasoning" should briefly explain your reasoning before making the decision.
The value of "decision" should have the following format: 'I keep [] dollars to myself and offer [] dollars to the other player.'
Replace [] with your choices.

Subsequently, a responder will then either accept or reject your proposal.
If they accept, then the money will be divided according to your proposal.
If they reject, you two will earn nothing.

This is round {round_num} of the game with {total_rounds - round_num} round(s) left.
Important: Please pretend that you are a human in the game with the following features when making the decision: {feature}
Please answer in the exact format.
'''

    return template


def ug_responder_prompt(sum_of_money, total_rounds, round_num, feature, round_history_str, proposer_earnings, responder_earnings, offered_amount, questionaire=False):
    template = f'''
Game Instructions:
In this game, you are the responder (described below).
Your goal is to maximize your total payoff over {total_rounds} rounds.
In each round, another player (a proposer) will first propose how to divide a sum of {sum_of_money} dollars between themselves and you.
As the responder, your task is to either accept or reject that proposal.
If you accept, then the money will be divided according to the proposal. 
If you reject, you two will earn nothing.
You will be given the choices and payoffs of both players in past rounds.
Your total payoff in this game will be the cumulative sum of the payoffs you obtain over {total_rounds} rounds.
'''
    
    if round_num == 1:
        template += f'''
Now let us begin the game!
Recall that you are the responder.

'''
    else:
        template += f'''
Recall that you are the responder.
You have played {round_num - 1} round(s) before.
Here is the history of the gameplay of previous rounds: {round_history_str}
Your total payoff so far: {responder_earnings} dollars;
The other player's total payoff so far: {proposer_earnings} dollars
'''

    if questionaire==False:
        template += f'''
Proposer's offer:
In this round, the proposer proposes to offer you {offered_amount} dollars while keeping the remaining {sum_of_money - offered_amount} dollars to themselves.
Do you accept or reject the offer?

Please provide a concise answer in this round by completing the following: '[].' with [] being either accept or reject.

If you accept, then the money will be divided according to the proposal. If you reject, you two will earn nothing.
This is round {round_num} of the game with {total_rounds - round_num} round(s) left.
Important: Please pretend that you are a human in the game with the following features when making the decision: {feature}
Please only answer one word: either accept or reject (no need to tell your reasoning).
'''
    else:
        template += f'''
Proposer's offer:
In this round, the proposer proposes to offer you {offered_amount} dollars while keeping the remaining {sum_of_money - offered_amount} dollars to themselves.
Do you accept or reject the above offer?

Please provide your answer in this round in a single-line JSON format with two keys: "reasoning" and "decision"
{{"reasoning": "...", "decision": "..."}}
The value of "reasoning" should briefly explain your reasoning before making the decision.
The value of "decision" should be just one word: either accept or reject.

If you accept, then the money will be divided according to the proposal. 
If you reject, you two will earn nothing.
This is round {round_num} of the game with {total_rounds - round_num} round(s) left.

Important: Please pretend that you are a human in the game with the following features when making the decision: {feature}
Please answer in the exact format.
'''
        
    return template

