from scipy.io.wavfile import read
def calc_distances(sound_file):
    min_val = 5000
    fs, data = read(sound_file)
    data_size = len(data)
    focus_size = int(0.15 * fs)
    
    focuses = []
    distances = []
    idx = 0
    
    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1
    return distances
    
def accept_test(pattern, test, min_error):
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattern):
        if not dt - test[i] < min_error:
            return False
    return True
pattern = calc_distances("knock-pattern.wav)
test = calc_distances("knock-test.wav")
min_error = 0.1
print accept_test(pattern, test, min_error)
