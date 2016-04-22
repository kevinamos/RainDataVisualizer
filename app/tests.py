from django.test import TestCase

# Create your tests here.



from django.test import TestCase


from app.models import RainDataStore



class RainDataStoreTest(TestCase):

	def setUp(self):
        	entry1=RainDataStore.objects.create(Rainfall_Amount=600, County='Kericho', Month='January')
	
	#this test creates an entry into the RainDataStore table and queries to check if the rainfall amount 		stored is correct amount that was entered

	def testRaindataPosted(self):

		get1=RainDataStore.objects.get(County='Kericho') 
      
		self.assertEqual(get1.Rainfall_Amount, 100)

	#tests if a duplicate entry is possible for a county that already has an entry for that month
	def testForMultipleEntries(self):
		entry1=RainDataStore.objects.create(Rainfall_Amount=700, County='Kericho', Month='January')
		self.assertEqual(entry1.status_code, 200)
		
		

