from sklearn import tree
model = tree.DecisionTreeClassifier(max_depth=9, criterion="entropy")
model.fit(X,y)
DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=9,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')

# .DOT files can be rendered to .PNGs, if you've already `brew install graphviz`.
tree.export_graphviz(model.tree_, out_file='tree.dot', feature_names=X.columns)

from subprocess import call
call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])