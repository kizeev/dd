# last char is missed in this solver


def decode_dd_vars(encoded_str):
    # Base64 alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
    
    result = ''
    temp = 0
    bit_count = 0
    
    for char in encoded_str:
        if char == '=':
            break
        
        idx = alphabet.index(char)
        
        temp |= idx << (18 - bit_count * 6)
        bit_count += 1
        
        if bit_count == 4:
            result += chr((temp >> 16) & 0xFF)
            result += chr((temp >> 8) & 0xFF)
            result += chr(temp & 0xFF)
            
            temp = 0
            bit_count = 0
    
    if bit_count:
    #     print('>>>', (temp >> 2) & 0xFF)
    #     print('>>>', chr(110))
        result += chr((temp >> 16) & 0xFF)
    # Handle remaining bytes
    # if bit_count > 1:
    #     result += chr((temp >> 10) & 0xFF)
    # if bit_count > 2:
    #     result += chr((temp >> 2) & 0xFF)
    
    return result

# Example usage
encoded_strings = ['z2v0tw91C2vqB3nPDgLVBG', 'zgrFua', 'zhzT', 'jgnKy18', 'Aw5KzxHLzerc', 'CgfYzw50rwXLBwvUDa', 'zgrFDW', 'zxjYB3i', 'zgf0yurVBwvxB3jRzxjfDMvUDe5HBwu', 'y2fSBa', 'zgrFrG', 'zgLZCgXHEq', 'y3jLyxrLrwXLBwvUDa', 'y2nZCG', 'y29VA2LL', 'zgvIDwC', 'B25LCNjVCG', 'B3bLBKrHDgfIyxnL', 'DhPW', 'DMmX', 'sw50zxjUzxqGrxHWBg9Yzxi', 'yNjFAa', 'CMfUzg9T', 'zM9UDezHBwLSEq', 'CMvTB3zLq2HPBgq', 'yNjVD3nLCMzSB3CTy29UDgfPBMvY', 'C3bSAxq', 'D3D3lG', 'zgrFCG', 'yxvKAw8VywfJoW', 'BgLUDxG', 'y2XPzw50wq', 'zgrFywK', 'Dg9W', 'DMnTCa', 'x193zwjKCML2zxjFC2nYAxb0x2z1BMm', 'BMf2AwDHDg9Y', 'Dw5RBM93BG', 'DMLKzw8Vm2DWCdS', 'y29UDgfJDhm', 'yML0BMvZCW', 'AM9PBG', 'tgLIzxjHDgLVBIbtyw5Z', 'zw51BwvYywjSzq', 'BxbFC3K', 'DgjJzq', 'Bw91C2v1Ca', 'C3rYx3nZ', 'rxjYB3i', 'DgHLBG', 'mJG4otiYrdrcrte5odC1mZbcneu1rdrbmtC5ntjd', 'zNvUy3rPB24', 'CMvTB3zLrxzLBNrmAxn0zw5LCG', 'ChvZAa', 'zgLS', 'zgrFywu', 'twfJ', 'yw5KCM9Pza', 'AwzVDG', 'AgfZt3DUuhjVCgvYDhK', 'z2X2za', 'AgnVDMrYmG', 'yxn5BMnOCM9UAxPLvgfZAW', 'ltK5otLWEa', 'zgrFsq', 'BxbFBxK', 'DMnVDhm', 'zgrFEq', 'AhjLzG', 'ugfSyxrPBM8', 'DM5K', 'ywn3Dhm', 'y2HHCKnVzgvbDa', 'twf0Aa', 'yMnS', 'y2XPzw50sgvPz2H0', 'Bw9KzwW', 'Bw91C2vKB3DU', 'BxbFDhi', 'DMnV', 'zgrFywC', 'zgrFsW', 'sfrntfzPzgvVrwXLBwvUDa', 'y2HPBgroB2rLCW', 'C3rYx29KyG', 'CgXHDgzVCM0', 'zgrFAq', 'ywnTyq', 'y29UDgvUDfDPBMrVDW', 'uKvorevsrvi', 'C3r5Bgu', 'BwLTzvr5CgvZ', 'C2v0vgLTzw91Da', 'v29YA2vYq2f1z2H0rxjYoIa', 'ywn3BxrZ', 'DMn3Dhm', 'y2f0y2G', 'zgrFzW', 'z2v0', 'DMnX', 'D2LU', 'yM9KEq', 'z2XYza', 'CNnFy2q', 'DMLKzw8VBxa0oYbJB2rLy3m9iMf2yZeUndjfmdffiG', 'zgrQC2TLEq', 'Au9t', 'BMfTzq', 'yxvKAw8Vm2DWCdS', 'q2fTyNjPyq', 'DMLKzw8', 'DMnTChrZ', 'yxvKAw8VBxa0oW', 'C2vSzG', 'igq6', 'Dg9tDhjPBMC', 'DhnFBxrW', 'DxnLCKfNzw50rgf0yq', 'odDgmdm3odHfnZG1rKyZmdfeotbcqJe5n0u1odaZ', 'z2v0q29UDgv4Da', 'C3fYDa', 'Bwf4', 'yxvKAw8VB2DNoYbJB2rLy3m9iNzVCMjPCYi', 'yxDL', 'AgvHza', 'zgrFwq', 't3rOzxi', 'CgXNz3q', 'u2vNBYbvsq', 'DhnFDhnH', 'ANnM', 'qw5KCM9Pza', 'DgvYBwLUyxrL', 'CgXVDMrYmG', 'z2v0t3DUuhjVCgvYDhLezxnJCMLWDg9Y', 'BM8GD29YA2vY', 'zgv2AwnLtwvTB3j5', 'CgXNCMu', 'B2zMC2v0v2LKDgG', 'C2nYzwvUwa', 'zgrFyG', 'CMvZB2X2zwrpChrPB25Z', 'zgf0yurVBwvuB29SCW', 'BxbFBxG', 'zgrFDG', 'AxnbCNjHEq', 'C3rHy2S', 'DMLKzw8VB2DNoYbJB2rLy3m9iNrOzw9Yysi', 'zgrFAG', 'A2v5C0rLBhrH', 'Aw5UzxjizwLNAhq', 'C2vYAwfSAxPLvg9tDhjPBMC', 'zxjY', 'ywmZ', 'DMnO', 'zgrFDq', 'zgrFBq', 'z2v0rwXLBwvUDhncEvrHz05HBwu', 'CgX1z2LUCW', 'x18KD2vIzhjPDMvYqxn5BMnfEgvJDxrVCG', 'y2HYB21L', 'Bg9JyxrPB24', 'C2L2za', 'zw1WDhK', 'Bw1TBw1TBw1TD3D3D3D3DW', 'zgrFzq', 'D2LUzg93CYbWAg9Uzq', 'ywnTChrZ', 'BwfJ', 'ChjT', 'AgnVDMrY', 'Bw10', 'zgrFEa', 'DMmXDhm', 'zgf0yq', 'AwrU', 'y29UC29Szq', 'y2fJAgvF', 'y2fUDMfZ', 'D2LKDgG', 'z2v0sgLNAevUDhjVChLwywX1zxm', 'BMnSywq', 'BNvHza', 'Dw5KzwzPBMvK', 'C3rYAw5N', 'yNjFB2G', 'AxbVza', 'D2rPzNjT', 'zgrFuW', 'zgvSzxrLqwXSrerdB29RAwvZ', 'yxvKAw8VD2f2oYbJB2rLy3m9iJeI', 'ChnU', 'zgf0yurVBwvpChrPB25Z', 'zgrFDgvZDgnVB2TPzt0XoYbWyxrOps87ifnHBwvtAxrLpuXHEa', 'zgrFywm', 'ChjVDg90ExbL', 'BgfUz3vHz2vZ', 'ndK5quuZndeYouzbneu0rKfcqZmXntGYqZmWnZve', 'rtqYntu5n0veounbqJC5mtHcmZvfqJiZrKverJKW', 'neuXnZLbnZmXmeneouiYmZqWrJG1rdKXoee5nKm4', 'Bwf0y2G', 'yMn0', 'CgXNB2y', 'x19ZzwXLBML1Bv9LDMfSDwf0zq', 'C2vSzw5PDw0TzxzHBhvHDgu', 'ywnTCdr0CW', 'DhLWzq', 'x2LMCMfTzvjLzG', 'zgrFyw0', 'DxnLCKXHBMD1ywDL', 'x19WCM90B19F', 'C3f0', 'z2v0qMf0DgvYEq', 'AxnuExbLu3vWCg9YDgvK', 'A2LUza', 'ywjZB2X1Dgu', 'C2XHDa', 'DMmZDhm', 'B2nWDa', 'u2fMyxjP', 'x19KCML2zxjFzxzHBhvHDgu', 'DMvUzg9Y', 'zgrFywe', 'igC6', 'zgrFywS', 'zgrFta', 'ywnTCdm', 'Bg9NmW', 'DgLTzvn0yw1W', 'CxvLCNLtzwXLy3rVCKfSBa', 'yNrVyq', 'zg9JDw1LBNrfBgvTzw50', 'CgX1', 'zgrFwa', 'x2rKDhD2', 'Bwf4vg91y2HqB2LUDhm', 'zw51BwvYyxrLrgv2AwnLCW', 'D2vIzhjPDMvY', 'nZmYmKyWnZC1nueYrte4mZDcmdvbmtHenJG3rJnd', 'CMvWBgfJzq', 'D2rPzG', 'CgXNB2q', 'ywmZDhm', 'C2nYzwvU', 'AxDNBa', 'qxbWBguGu0qGr290AgLJie5LBW', 'BwvZC2fNzq', 'A2v5CW', 'Cg9ZDe1LC3nHz2u', 'tgLUDxG', 'yxn5BMndAgfSBgvUz2vgAw5PC2HLza', 'zgrFza', 'CxvLCNLtzwXLy3rVCG', 'CMv2B2TLt2jQzwn0vvjm', 'zgrFuG', 'y2HLy2TnB3vZzvbVC2L0Aw9U', 'zwnWyW', 'oezfmengn0y4quiZmevdntG4ntK5rdGWndzfrdbf', 'v2LUzg93CYbqAg9Uzq', 'zgrFvG', 'vu5nqvnlrurFvKvore9sx1DfqKDm', 'y2zWCa', 'ywnHyq', 'twLTzvr5CgvbCNjHEq', 'DMn3', 'q2HYB21L', 'q3vZDg9TrxzLBNq', 'vg91y2HfDMvUDa', 'ywnTCa', 'zgLZCgf0y2HfDMvUDa', 'C3b3BG', 'AxnxB3jRzxjbDMfPBgfIBgu', 'jgnKy19HC2rQzMXHC3v0B3bMAhzJwKXTy2zSxW', 'Aw5UzxjxAwr0Aa', 'D2vIzhjPDMvYq29TBwfUza', 'z2v0vgLTzxPVBMvpzMzZzxq', 'DMLKzw8VBxbLzW', 'CMv0DxjU', 'zg9JDw1LBNq', 'BwfUDwfSq2HLy2TozwvKzwq', 'zgrFywi', 'zgrFqq', 'DxnLCKfNzw50', 'DMmZ', 'ywXIlNjLzgrPDa', 'yMr0', 'Dg9mB3DLCKnHC2u', 'yMLUza', 'yxvKAw8VEc1Tnge7', 'BMrKyW', 'yxvKAw8', 'zgrFyw8', 'zgrFyw4', 'z2v0sw5MB0nSAwnR', 'BMHP', 'yL9L', 'Bgv2zwW', 'zgrFEG', 'y2fUugXHEvr5Cgu', 'y2XPzw50wa', 'zgrFsa', 'zgrFvq', 'CgfYC2vjBNq', 'yMnKyq', 'yxvKAw8VzMXHyZS', 'CgXVDMrY', 'yxvKAw8VD2vIBtS', 'tM90BYbtyw5Z', 'ywnVDhm', 'zgrFywy', 'zw1K', 'DNbICq', 'DhjPzgvUDa', 'rhjVAwqGu2fUCW', 'yNvPBgrjra', 'B3jPzw50yxrPB24', 'u29Uz3rP', 'CxvLCNK', 'BgvUz3rO', 'zxDZAq', 'Aw5KzxHpzG', 'ywnM', 'B3bY', 'B2jQzwn0', 'zNrZB3zKCJi', 'zxH0zxjUywW', 'u1zhrgLZy2fYzevSzw1LBNq', 'C2XPy2u', 'BgfIzwW']
for i in encoded_strings:
    print(f"Encoded: {i}")
    decoded_result = decode_dd_vars(i)
    print(f"Decoded: {decoded_result}\n")

