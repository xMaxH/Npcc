import sys
import graphviz


class production():
    all_productions = []

    def __init__(self, name):
        self.name = name
        self.productions: list[production] = []
        self.term: bool
        self.first: set = set([])

    @staticmethod
    def add_prototypes(productions: dict):
        for nam in list(map(lambda x: x[0], productions)):
            production.all_productions.append(production(nam))

    @staticmethod
    def find_production(name):
        for prod in production.all_productions:
            if prod.name == name:
                return prod
        print("couldnt find " + name)
        raise Exception
        return

    def __repr__(self) -> str:
        ret = ""
        if self.term:
            ret = self.productions[0][0]
        else:
            for prod in self.productions:
                ret += "["
                for symb in prod:
                    ret += symb.name + "," + str(symb.term) + ":"
                ret += "]"
        return "[" + self.name + "," + str(self.term) + "->" + ret + "]" + "\n"

    @staticmethod
    def update_productions(productions: list):
        for prod in productions:
            cur = production.find_production(prod[0])
            if prod[1][0][0].startswith("\""):
                cur.term = True
                cur.productions = prod[1]
            else:
                cur.term = False
                for single_prod in prod[1]:
                    cur.productions.append(
                        [production.find_production(x) for x in single_prod])

    def set_first(self):
        if self.term == True:
            return set([self.name])
        else:
            for prod in self.productions:
                self.first = self.first.union(prod[0].set_first())
            return self.first
    def check_ll_one(self) -> bool:
        for production in self.productions:
            for production2 in [x for x in self.productions if not x == production]:
                factor = longest_factor(production, production2)
                if factor == len(production) or factor == len(production2):
                    continue
                #print("longest factor for" + " " + self.name + " " + str(factor) + " " + str(set(production[factor].first).union(production2[factor].first)))
                if not set(production[factor].first).isdisjoint(production2[factor].first):
                    return False
        return True
    @staticmethod
    def verify() -> bool:
        lst = [prod.check_ll_one() for prod in production.all_productions]
        ret = str(all(lst))
        print("The grammar has no first-first conflicts: " + ret)
def longest_factor(lst1, lst2):
    for i in range(min([len(lst1), len(lst2)])):
        if not lst1[i] == lst2[i]:
            return i
    return min([len(lst1), len(lst2)])

class bnf_syntax_tree():
    dot = graphviz.Digraph('graph', comment='the syntax graph')  
    def __init__(self, productions: production):
        self.productions = productions
        self.out = []
        bnf_syntax_tree.dot.node(str(id(self)), self.productions.name)
        if not productions.term:
            for production in productions.productions:
                tree = self
                for symbol in production:
                    if symbol == productions:
                        tree.out.append(self)
                    else:
                        tree.out.append(bnf_syntax_tree(symbol))
                    bnf_syntax_tree.dot.edge(str(id(tree)), str(id(tree.out[-1])))
                    bnf_syntax_tree.dot.render(directory='tree')
                    tree = tree.out[-1]
    def add(self, symbol):
        self.out.append(symbol)
def main2():
    productions: list
    with open(sys.argv[1]) as f:
        content = f.read()
    productions = gen_productions(remove_comments_empty(content.splitlines()))
    production.add_prototypes(productions)
    production.update_productions(productions)
    #tree = bnf_syntax_tree(production.find_production("program"))
    #print(tree)
    print(productions)
    print(production.all_productions)
    for prod in production.all_productions:
        prod.set_first()
    #for prod in production.all_productions:
    #srint(prod.name + " " + str(prod.first))
    #for prod in production.all_productions:
    #    print(prod.name + " " + str(prod.check_ll_one()))
    production.verify()


def remove_comments_empty(string: str):
    ret = []
    for line in string:
        if not line.startswith("//") and not line == "" and not line.startswith("#"):
            ret.append(line)
    return ret


def gen_productions(lst: list):
    ret = []
    for line in lst:
        splitted = line.split("::=")
        right = splitted[1].strip()
        left = splitted[0].strip()
        if right.startswith("\""):
            prods = [[right]]
        else:
            prods = [list(map(lambda y: y.replace(">", "").replace("<", "").replace(
                "?", ""), x.strip().split())) for x in right.split("|")]
        ret.append([left, prods])
    return ret


if __name__ == '__main__':
    main2()
