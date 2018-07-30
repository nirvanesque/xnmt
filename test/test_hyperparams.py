import unittest

from xnmt.attenders import MlpAttender
from xnmt.batchers import mark_as_batch, Mask, SrcBatcher
from xnmt.bridges import CopyBridge
from xnmt.decoders import AutoRegressiveDecoder
from xnmt.embedders import SimpleWordEmbedder
from xnmt.eval_tasks import LossEvalTask
from xnmt import events
from xnmt.input_readers import PlainTextReader
from xnmt.recurrent_transducers import UniLSTMSeqTransducer, BiLSTMSeqTransducer
from xnmt.loss_calculators import AutoRegressiveMLELoss
from xnmt.optimizers import AdamTrainer
from xnmt.param_collections import ParamManager
from xnmt.pyramidal import PyramidalLSTMSeqTransducer
from xnmt.transforms import NonLinear
from xnmt.translators import DefaultTranslator
from xnmt.scorers import Softmax
from xnmt.vocabs import Vocab

from xnmt.hyper_params import *
from xnmt.specialized_encoders.segmenting_encoder.segmenting_encoder import *
from xnmt.specialized_encoders.segmenting_encoder.segmenting_composer import *

class TestSanityHyperParameter(unittest.TestCase):
  def setUp(self):
    events.clear()

  def test_scalar_operator(self):
    c = Scalar(5)
    self.assertEqual(c+1, 6)
    self.assertEqual(c-1, 4)
    self.assertEqual(c*2, 10)
    self.assertEqual(c/2, 2.5)
    self.assertEqual(c//2, 2)
    self.assertEqual(-c, -5)
    self.assertEqual(+c, 5)
    self.assertEqual(c >= 5, True)
    self.assertEqual(c > 5, False)
    self.assertEqual(c <= 5, True)
    self.assertEqual(c != 5, False)
    self.assertEqual(c < 5, False)
    self.assertEqual(c == 5, True)
    self.assertEqual(c ** 2, 25)

  def test_defined_sequence(self):
    ds = DefinedSequence([10, 20, 30])
    ds.on_new_epoch()
    self.assertEqual(ds, 10)
    ds.on_new_epoch()
    self.assertEqual(ds, 20)
    ds.on_new_epoch()
    self.assertEqual(ds, 30)
    ds.on_new_epoch()
    self.assertEqual(ds, 30)

# Test will be made after there is an example to test serialized model
#class TestPersistenceHyperParameter(unittest.TestCase):
#  def setUp(self):
#    events.clear()
#    ParamManager.init_param_col()
#    self.tail_transformer = TailSegmentTransformer()
#    self.segment_encoder_bilstm = BiLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim)
#    self.segment_embed_encoder_bilstm = BiLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim)
#    self.segment_composer = SegmentComposer(encoder=self.segment_encoder_bilstm,
#                                            transformer=self.tail_transformer)
#    self.src_reader = PlainTextReader()
#    self.trg_reader = PlainTextReader()
#    self.loss_calculator = AutoRegressiveMLELoss()
#    self.segmenting_encoder = SegmentingSeqTransducer(
#      embed_encoder = self.segment_embed_encoder_bilstm,
#      segment_composer =  self.segment_composer,
#      final_transducer = BiLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim),
#      src_vocab = self.src_reader.vocab,
#      trg_vocab = self.trg_reader.vocab,
#      embed_encoder_dim = layer_dim,
#      length_prior = 3.3
#      length_prior_alpha = DefinedSequence([1,2,3,4])
#    )
#    self.model = DefaultTranslator(
#      src_reader=self.src_reader,
#      trg_reader=self.trg_reader,
#      src_embedder=SimpleWordEmbedder(emb_dim=layer_dim, vocab_size=100),
#      encoder=self.segmenting_encoder,
#      attender=MlpAttender(input_dim=layer_dim, state_dim=layer_dim, hidden_dim=layer_dim),
#      trg_embedder=SimpleWordEmbedder(emb_dim=layer_dim, vocab_size=100),
#      decoder=AutoRegressiveDecoder(input_dim=layer_dim,
#                                    rnn=UniLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim,
#                                                             decoder_input_dim=layer_dim, yaml_path="decoder"),
#                                    transform=AuxNonLinear(input_dim=layer_dim, output_dim=layer_dim,
#                                                           aux_input_dim=layer_dim),
#                                    scorer=Softmax(vocab_size=100, input_dim=layer_dim),
#                                    trg_embed_dim=layer_dim,
#                                    bridge=CopyBridge(dec_dim=layer_dim, dec_layers=1)),
#
#    )
#    self.model.set_train(True)
#
#    self.layer_dim = layer_dim
#    self.src_data = list(self.model.src_reader.read_sents("examples/data/head.ja"))
#    self.trg_data = list(self.model.trg_reader.read_sents("examples/data/head.en"))
#    my_batcher = xnmt.batcher.TrgBatcher(batch_size=3)
#    self.src, self.trg = my_batcher.pack(self.src_data, self.trg_data)
#    dy.renew_cg(immediate_compute=True, check_validity=True)

if __name__ == '__main__':
  unittest.main()