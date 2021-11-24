from grammar_conv import *

def cnf_file_to_dict(file):
    """
    Takes a CNF file and returns a dictionary of clauses.
    """
    clauses = {}
    with open(file, 'r') as f:
        for line in f:
            prod = line.split(" -> ")
            if clauses.get(prod[0]) is None:
                clauses[prod[0]] = [prod[1].strip()]
            else:
                clauses[prod[0]].append(prod[1].strip())
    return clauses

def cnf_file_to_dict_indra(cfg_file):
    """
    Takes a CNF file and returns a dictionary of clauses.
    """
    clauses = {}
    cnf = convert_grammar(read_grammar(cfg_file))
    for rule in cnf:
        if clauses.get(rule[0]) is None:
            value = rule[1:]
            value = " ".join([str(x) for x in value])
            clauses[rule[0]] = [value]
        else:
            value = rule[1:]
            value = " ".join([str(x) for x in value])
            clauses[rule[0]].append(value)
    return clauses

# print(cnf_file_to_dict_indra("cfg_process.txt"))