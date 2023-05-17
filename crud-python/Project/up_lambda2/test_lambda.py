import main_utils
import unittest
unittest.TestLoader.sortTestMethodsUsing = None

class Test(unittest.TestCase):
	def test_a_setup_class(self):
		print('\r\nCreate test case...')
		args = {
			'Environment': {
				'Variables': {
					'LOCALSTACK': 'True'
				}
			}
		}
		main_utils.create_lambda('lambda', **args)
		main_utils.create_bucket('hands-on-cloud-bucket')
	def test_b_invoke_function_and_response(self):
		print('\r\nInvoke test case...')
		payload = main_utils.invoke_function('lambda')
		bucket_objects = main_utils.list_s3_bucket_objects('hands-on-cloud-bucket')
		self.assertEqual(bucket_objects, ['hands-on-cloud.txt'])
	def test_c_teardown_class(self):
		print('\r\nDelete test case...')
		main_utils.delete_lambda('lambda')
		main_utils.delete_bucket('hands-on-cloud-bucket')
