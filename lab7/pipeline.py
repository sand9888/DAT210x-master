from sklearn.pipeline import Pipeline

svc = svm.SVC(kernel='linear')
pca = RandomizedPCA()

pipeline = Pipeline([
  ('pca', pca),
  ('svc', svc)
])
pipeline.set_params(pca__n_components=5, svc__C=1, svc__gamma=0.0001)
pipeline.fit(X, y)




from sklearn.base import TransformerMixin

class ModelTransformer(TransformerMixin):
  def __init__(self, model):
    self.model = model

  def fit(self, *args, **kwargs):
    self.model.fit(*args, **kwargs)
    return self

  def transform(self, X, **transform_params):
    # This is the magic =)
    return DataFrame(self.model.predict(X))