import random
import time

# Ορισμός seed σε 2565.
random.seed(2565)

# Λίστα για αποθήκευση των τυχαίων αριθμών πιστωτικών καρτών.
numbers = []

# Λεξικό για αποθήκευση των χρεώσεων για κάθε κάρτα.
# Στήν θέση [0] θα αποθηκευτεί το ποσό χρεώσεων και στην θέση [1] το πλήθος των χρεώσεων.
card_charges = {}

# Δημιουργία 20000 τυχαίων αριθμών πιστωτικών καρτών.
for _ in range(20000):
    # Δημιουργία τυχαίων 16 ψήφιων αριθμών.
    random_number = random.randint(0000000000000000, 9999999999999999)
    # Προσθήκη των τυχαίων αριθμών στην λίστα numbers.
    numbers.append(random_number)

# Δημιουργία 1.000.000 τυχαίων χρεώσεων.
for _ in range(1_000_000):
    # Επιλογή τυχαίου αριθμού κάρτας από τη λίστα numbers.
    random_number = random.choice(numbers)
    # Επιλογή τυχαίου ποσού χρέωσης από 10 έως 1000 ευρώ.
    random_amount = random.randint(10, 1000)
    
    # Αν ο αριθμός κάρτας δεν υπάρχει στο λεξικό, προσθέτεται και αρχικοποιείται μαζί με το αντοίστιχο ποσό χρέωσης.
    if random_number not in card_charges:
        card_charges[random_number] = [random_amount, 1]
    else:
        # Ενώ, αν προυοπάρχει ο αριθμός κάρτας στό λεξικό προσθέτεται το ποσό χρέωσης στο ήδη υπάρχον ποσό και αυξάνεται κατά 1 το πλήθος των συναλλαγών.
        card_charges[random_number][0] += random_amount
        card_charges[random_number][1] += 1

# Αρχή χρονομέτρησης.
start = time.time()

# Υπολογισμός των απαιτούμενων ερωτημάτων, με χρήση των αντίστοιχων συναρτήσεων και σαν κρτιτίριο την αντίστοιχη θέση του λεξικού. 
min_total_payment_card = min(card_charges, key=lambda card: card_charges[card][0])
max_total_payment_card = max(card_charges, key=lambda card: card_charges[card][0])
min_transaction_count_card = min(card_charges, key=lambda card: card_charges[card][1])
max_transaction_count_card = max(card_charges, key=lambda card: card_charges[card][1])

# Τέλος χρονομέτρησης.
elapsed_time = time.time() - start

# Εμφάνιση των αποτελεσμάτων μαζί με τα ποσά πληρωμών και το πλήθος συναλλαγών.
print(f"Η κάρτα με το μικρότερο συνολικό ποσό πληρωμών είναι η {min_total_payment_card} με ποσό {card_charges[min_total_payment_card][0]} ευρώ.")
print(f"Η κάρτα με το μεγαλύτερο συνολικό ποσό πληρωμών είναι η {max_total_payment_card} με ποσό {card_charges[max_total_payment_card][0]} ευρώ.")
print(f"Η κάρτα με το μικρότερο πλήθος συναλλαγών είναι η {min_transaction_count_card} με {card_charges[min_transaction_count_card][1]} χρεώσεις.")
print(f"Η κάρτα με το μεγαλύτερο πλήθος συναλλαγών είναι η {max_transaction_count_card} με {card_charges[max_transaction_count_card][1]} χρεώσεις.")

# Εμφάνιση συνολικού χρόνου λειτουργιών.
print(f"Ο συνολικός χρόνος εκτέλεσης είναι {elapsed_time:.2f} δευτερόλεπτα.")



# Kλάση για την υλοποίηση ενός πίνακα κατακερματισμού με γραμμική διερεύνηση.
class Linear_Probing_Hash_Table:
    
    
    # Συνάρτηση αρχικοποίησης του πίνακα κατακερματισμού.
    def __init__(self, size=101):
        # Το default size του πίνακα κατακερματισμού είναι 101.
        self.size = size 
        # Δημιουργία μιας λίστας με size στοιχεία, όλα αρχικοποιημένα στην τιμή None.
        # Η τιμή None αναπαριστά την έλλειψη ή την απουσία μίας τιμής.
        self.table = [None] * size
        # Αρχικό load fαctor = 0%.
        self.load_factor = 0
        
        
    # Συνάρτηση κατακερματισμού με χρήση mod.
    def hash_function(self, key):
        return key % self.size
        
        
    # Συνάρτηση εισγωγής ενός ζευγαριού (key, value) στον πίνακα κατακερματισμού.
    def put(self, key, value):
        # Έλεγχος για αναγκαίο rehash του πίνακα κατακερματισμού, αν το load factor >= 70%.
        if self.load_factor >= 0.7:
            self.rehash()
        # Υπολογισμός του δείκτη (index) όπου θα αποθηκευτεί ένα κλειδί (key) στον πίνακα κατακερματισμού.
        index = self.hash_function(key)
        # Γραμμική διερεύνηση για εύρεση κενής θέσης.
        # Η while επαναλαμβάνεται μέχρι να βρεθεί μια κενή θέση στον πίνακα.
        # Κάθε φορά που εκτελείται η while, ο δείκτης (index) αυξάνεται κατά 1 και υπολογίζεται ο νέος δείκτης με χρήση του υπολοίπου της διαίρεσης με το μέγεθος του πίνακα ((index + 1) % self.size).
        while self.table[index] is not None:
            index = (index + 1) % self.size
        # Εισαγωγή ενός στοιχείου στον πίνακα.
        self.table[index] = (key, value)
        # Ενημέρωση του συντελεστή φόρτωσης.
        self.load_factor = (self.load_factor * 2 + 1) / self.size


    # Συνάρτηση αναζήτησης ενός κλειδού απο τον πίνακα κατακερματισμού.
    def get(self, key):
        index = self.hash_function(key)
        # Η while εκτελείται όσο η θέση του πίνακα (self.table[index]) έχει κάποιο στοιχείο σε αυτή την θέση.
        while self.table[index] is not None:
            # Σε κάθε επανάληψη, ελέγχουμε αν το κλειδί του τρέχοντος στοιχείου είναι ίσο με το κλειδί που ψάχχνουμε.  
            if self.table[index][0] == key:
                #Αν βρεθεί, επιστέφεται η σχετική τιμή.    
                return self.table[index][1]
            # Αν το στοιχείο δεν είναι αυτό που αναζητούμε, μετακινούμαστε στο επόμενο. 
            # Η επιλογή του επόμενου στοιχείου γίνεται με χρήση γραμμική διερεύνησης.
            index = (index + 1) % self.size
        # Επιστροφή 'None' αν δε βρεθεί το κλειδί.
        return None


    # Συνάρτηση αφαίρεσης ενός κλειδιού από τον πίνακα κατακερματισμού.
    def remove(self, key):
        index = self.hash_function(key)
         # Η while εκτελείται όσο η θέση του πίνακα έχει κάποιο στοιχείο σε αυτή την θέση.
        while self.table[index] is not None:
            # Έλεγχος για αν το κλειδί βρίσκεται στην τρέχουσα θέση.
            if self.table[index][0] == key:
                # Αν ναι, γίνεται αφαίρεση του ζευγαριού κλειδί-τιμής θέτοντας το περιεχόμενο σε None.
                self.table[index] = None
                return
            # Μετακίνηση στην επόμενη θέση χρησιμοποιώντας γραμμική διερεύνηση.
            index = (index + 1) % self.size
            
            
    # Συνάρτηση αύξησης του μεγέθους του πίνακα κατακερματισμού στον επόμενο τουλάχιστον διπλάσιο πρώτο αριθμό.
    def rehash(self):
        # Αρχικά, διπλασιάζουμε το μέγεθος του πίνακα κατακερματισμού.
        new_size = self.size * 2
        # Εύρεση του επόμενου πρώτου αριθμού που είναι διπλάσιος του new_size.
        while not self.is_prime(new_size):
            new_size += 1
        # Ο νέος πίνακας κατακερματισμού αρχικοποιείται με κενές θέσεις.
        new_table = [None] * new_size
        # Επανατοποθέτηση υπαρχόντων στοιχείων στο νέο μέγεθος πίνακα για κάθε ζεύγος item που δεν έχει τιμή 'Νονε'.
        for item in self.table:
            if item is not None:
                # Unpacking του tuple item σε δύο μεταβλητές, key και value.
                key, value = item 
                # Υπολογισμός νέου δείκτη (index) για το νέο μέγεθος.
                index = self.hash_function(key)
                # Εύρεση νέας κενής θέσης με γραμμική διερεύνηση.
                while new_table[index] is not None:
                    index = (index + 1) % new_size
                # Το στοιχείο τοποθετείται στην εντοπισμένη κενή θέση του νέου πίνακα, βάζοντας το tuple (key, value).
                new_table[index] = (key, value)
        # Ενημέρωση του μεγέθους και του πίνακα κατακερματισμού.
        self.size = new_size


    # Συνάρτηση ελέγχου για το αν ένας αριθμός είναι πρώτος.
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
