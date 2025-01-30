from pecanpy import pecanpy
from gensim.models import Word2Vec
from scipy import triu

p_q = {
    1: 1,
    0.5: 1,
    1: 0.5
}

vector_size = 512

edges_path = "../data/networks"
embeddings_path = "../data/embeddings"

edge_files = ["BioGRID.edg", "STRING-EXP.edg"]
new_embedding_files_names = [
    "BioGRID_1_1.emd", "BioGRID_point5_1.emd", "BioGRID_1_point5.emd",
    "STRING-EXP_1_1.emd", "STRING-EXP_point5_1.emd", "STRING-EXP_1_point5.emd"
]

graph_settings = {
    "BioGRID.edg": {"weighted": False},
    "STRING-EXP.edg": {"weighted": True}
}

embedding_idx = 0
for edge_file in edge_files:
    for p, q in p_q.items():
        g = pecanpy.SparseOTF(p=p, q=q, workers=1, verbose=False)
        g.read_edg(f"{edges_path}/{edge_file}", 
                   weighted=graph_settings[edge_file]["weighted"], 
                   directed=False)

        walks = g.simulate_walks(num_walks=10, walk_length=80)

        w2v_model = Word2Vec(
            walks, 
            vector_size=vector_size, 
            window=3, 
            min_count=0, 
            sg=1, 
            workers=1, 
            epochs=1
        )

        w2v_model.wv.save_word2vec_format(f"{embeddings_path}/{new_embedding_files_names[embedding_idx]}")
        print(f"{new_embedding_files_names[embedding_idx]} created successfully...")
        embedding_idx += 1


# from pecanpy import pecanpy
# from gensim.models import Word2Vec
# # load graph object using SparseOTF mode
# g = pecanpy.SparseOTF(p=1, q=0.5, workers=1, verbose=False)
# g.read_edg("../data/networks/STRING-EXP.edg", weighted=True, directed=False)
# # generate random walks
# walks = g.simulate_walks(num_walks=10, walk_length=80)
# # use random walks to train embeddings
# w2v_model = Word2Vec(walks, vector_size=512, window=3, min_count=0, sg=1, workers=1, epochs=1)
# w2v_model.wv.save_word2vec_format("../data/embeddings/STRING-EXP_1_point5.emd")