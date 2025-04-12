% A6.pl

% Define rules for diagnosing diseases based on symptoms
disease(flu) :-
    is_true("Do you have fever?"),
    is_true("Do you have body ache?"),
    is_true("Do you have cough?").

disease(cold) :-
    is_true("Do you have sneezing?"),
    is_true("Do you have sore throat?"),
    is_true("Do you have mild fever?").

disease(malaria) :-
    is_true("Do you have chills?"),
    is_true("Do you have high fever?"),
    is_true("Do you have sweating?").

% Ask user for input and check if it is 'yes.'
is_true(Question) :-
    format("~s (yes/no): ", [Question]),
    read(Response),
    Response == yes.

% Start diagnosis
start_diagnosis :-
    nl,
    write('Welcome to the Medical Diagnosis Expert System'), nl,
    write('Please answer the following questions with "yes" or "no".'), nl, nl,
    (   disease(Disease) -> 
        format('You may have ~w.\n', [Disease]),
        start_diagnosis
    ;   write('Sorry, your symptoms do not match any known disease in our system.\n'),
        start_diagnosis 
    ).