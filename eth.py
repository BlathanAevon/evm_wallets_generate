import csv
from web3.auto import w3
from eth_account import Account
from eth_account.hdaccount import generate_mnemonic


Account.enable_unaudited_hdwallet_features()


# Generate a new wallet and mnemonic
def generate_wallet():
    mnemonic = generate_mnemonic(12, "english")
    account = w3.eth.account.from_mnemonic(mnemonic)
    private_key = account._private_key
    return private_key, mnemonic

# Create a CSV file and write the wallet information
def write_to_csv(wallet_data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["WALLET", "PRIVATE KEY", "SEED PHRASE"])

        for private_key, mnemonic in wallet_data:
            address = Account.from_key(private_key).address
            csv_writer.writerow([address, private_key.hex(), mnemonic])

# Number of wallets to generate
num_wallets = int(input("How many wallets to generate: "))

# Generate wallets and mnemonic phrases
wallet_data = [generate_wallet() for _ in range(num_wallets)]

# Write the wallet information to a CSV file
csv_filename = "evm_wallets.csv"
write_to_csv(wallet_data, csv_filename)

print(f"{num_wallets} wallets generated and saved to {csv_filename}")
