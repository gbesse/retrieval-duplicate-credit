import unittest,copy,json
from retrieval_duplicate_credit import run
DEMO={'ranking': [{'id': 'a1', 'content_id': 'A'}, {'id': 'a2', 'content_id': 'A'}, {'id': 'b', 'content_id': 'B'}], 'relevance': {'A': True, 'B': False}, 'k': 2}
class DomainTests(unittest.TestCase):
 def test_duplicate_recall_can_exceed_one(self):
  x=run(DEMO);self.assertEqual(x['naive_document_metrics']['recall_at_k'],2);self.assertEqual(x['canonical_content_metrics']['recall_at_k'],1);self.assertEqual(x['canonical_content_metrics']['precision_at_k'],.5)
 def test_relevance_unit_not_document_identifier(self):
  x=run(DEMO);self.assertEqual(x['duplicate_document_ids'],['a2']);self.assertEqual(x['deduplicated_ranking_ids'],['a1','b'])
 def test_unjudged_not_assumed_irrelevant(self):
  x=copy.deepcopy(DEMO);del x['relevance']['B']
  with self.assertRaises(ValueError):run(x)
