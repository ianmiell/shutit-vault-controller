from shutit_module import ShutItModule

class shutit_vault_controller(ShutItModule):


	def build(self, shutit):
		shutit.install('git')
		shutit.send('git clone https://github.com/kelseyhightower/vault-controller.git')
		shutit.send('cd vault-controller')
		#https://github.com/kelseyhightower/vault-controller/blob/master/docs/deployment-guide.md
		#https://github.com/kelseyhightower/vault-controller/blob/master/docs/example-usage.md
		#https://github.com/kelseyhightower/vault-controller/blob/master/docs/microservice-tutorial.md
		shutit.pause_point('')
		return True

	def get_config(self, shutit):

		return True

	def test(self, shutit):

		return True

	def finalize(self, shutit):

		return True

	def is_installed(self, shutit):

		return False

	def start(self, shutit):

		return True

	def stop(self, shutit):

		return True

def module():
		return shutit_vault_controller(
			'git.shutit_vault_controller.shutit_vault_controller', 1591410362.0001,
			description='',
			maintainer='',
			delivery_methods=['bash'],
			depends=['shutit-library.minikube.minikube']
		)
