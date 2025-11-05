function caesarCipher(message, shift) {
    return message.split("").map(char => {
        if (char >= 'A' && char <= 'Z') {
            return String.fromCharCode((char.charCodeAt(0) - 65 + shift) % 26 + 65);
        } else if (char >= 'a' && char <= 'z') {
            return String.fromCharCode((char.charCodeAt(0) - 97 + shift) % 26 + 97);
        } else {
            return char;
        }
    }).join("");
}

function caesarDecode(message, shift) {
    return caesarCipher(message, (26 - shift) % 26);
}

function generateCipher() {
    const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
    const shuffled = [...alphabet].sort(() => Math.random() - 0.5);
    const map = {};
    for (let i = 0; i < 26; i++) {
        map[alphabet[i]] = shuffled[i];
    }
    return map;
}

function substitutionCipher(message, cipherMap) {
    return message.split("").map(char => {
        if (char >= 'A' && char <= 'Z') {
            return cipherMap[char.toLowerCase()].toUpperCase();
        } else if (char >= 'a' && char <= 'z') {
            return cipherMap[char];
        } else {
            return char;
        }
    }).join("");
}

function substitutionDecode(message, cipherMap) {
    const reverseMap = {};
    for (let key in cipherMap) {
        reverseMap[cipherMap[key]] = key;
    }

    return message.split("").map(char => {
        if (char >= 'A' && char <= 'Z') {
            return reverseMap[char.toLowerCase()].toUpperCase();
        } else if (char >= 'a' && char <= 'z') {
            return reverseMap[char];
        } else {
            return char;
        }
    }).join("");
}