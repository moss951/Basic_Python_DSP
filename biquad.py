def process(current_input, prev1_input, prev1_output, prev2_input, prev2_output, a0, a1, a2, b0, b1, b2):
    processed_current_input = (b0 / a0) * current_input
    processed_prev1_input = (b1 / a0) * prev1_input
    processed_prev2_input = (b2 / a0) * prev2_input
    processed_prev1_output = (a1 / a0) * prev1_output
    processed_prev2_output = (a2 / a0) * prev2_output

    return processed_current_input + processed_prev1_input + processed_prev2_input - processed_prev1_output - processed_prev2_output