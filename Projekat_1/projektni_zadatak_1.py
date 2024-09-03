import subprocess

def run_scripts(scripts):
    processes = []

    for script in scripts:
        print(f"running.. {script}...")
        process = subprocess.Popen(['python', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)

    for process in processes:
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(stdout.decode('utf-8'))
        else:
            print(f"Proces {process.pid} je naišao na grešku.")
            print(stderr.decode('utf-8'))

if __name__ == "__main__":
    # Lista vaših Python skripti
    scripts = [
        'entropija.py',
        'huffman.py',
        'shannon_fano.py',
        'lz77.py',
        'lzw.py',
        'proveri_gubitke.py'
    ]
    
    run_scripts(scripts)
