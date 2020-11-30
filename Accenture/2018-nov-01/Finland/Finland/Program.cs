using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Jint;

namespace Finland
{
    static class Program
    {

        private static string enteredpasscode = "";
        private static readonly string a = "slsd!#$sa";
        private static readonly string b = "#$KD213ks";
        private static readonly string c = "@13Ag1S4d3f6g123";
        public static uint[] fff = new uint[3] { 45U, 13U, 15U };

        private static void Main(string[] args)
        {
            /*
            for (int s = 1; s <= 15; ++s)
            {
                Console.WriteLine(s + ": " + getString(s));
            }
            Console.WriteLine("CBDu>pL\x08m^1\x10l4nj\x11g_\x05mJ*\x12W4rj)Y_\x07mw![o\x19@<9d@\x07Ag%To4nx");
            for (int index = 0; index < args.Length; ++index)
            {
                if (args[index] == "-passcode" && args.Length > index + 1)
                    Program.enteredpasscode = args[index + 1];
            }
            Program.check();
            Console.WriteLine(Program.getString(1));
            if (!Program.checkPasscode(true))
                Environment.Exit(1);
            if (!Program.checkPasscode(false))
                return;
            Program.continue1();
            */
            Console.WriteLine(EncryptOrDecrypt("CBDu>pm^1l4njg_mJ*W4rj)Y_mw![o@<9d@zg%To4nx"));
        }

        private static bool checkPasscode(bool print)
        {
            if (Program.enteredpasscode != "")
            {
                if (print)
                    Console.Write(Program.getString(9));
                if (Program.enteredpasscode != Program.getString(7))
                {
                    Thread.Sleep(1000);
                    Console.WriteLine(Program.getString(8));
                    return false;
                }
                if (print)
                    Console.WriteLine(Program.getString(10));
                return true;
            }
            Console.WriteLine(Program.getString(6));
            return false;
        }

        private static void continue1()
        {
            if (!File.Exists(Program.getString(12)))
            {
                File.AppendAllText(Program.getString(12), Program.getString(14));
                Console.WriteLine(Program.getString(11));
            }
            byte[] numArray = new byte[52]
            {
        (byte) 67,
        (byte) 66,
        (byte) 68,
        (byte) 117,
        (byte) 62,
        (byte) 112,
        (byte) 76,
        (byte) 8,
        (byte) 109,
        (byte) 94,
        (byte) 49,
        (byte) 16,
        (byte) 108,
        (byte) 52,
        (byte) 110,
        (byte) 106,
        (byte) 17,
        (byte) 103,
        (byte) 95,
        (byte) 5,
        (byte) 109,
        (byte) 74,
        (byte) 42,
        (byte) 18,
        (byte) 87,
        (byte) 52,
        (byte) 114,
        (byte) 106,
        (byte) 41,
        (byte) 89,
        (byte) 95,
        (byte) 7,
        (byte) 109,
        (byte) 119,
        (byte) 33,
        (byte) 91,
        (byte) 111,
        (byte) 25,
        (byte) 64,
        (byte) 60,
        (byte) 57,
        (byte) 100,
        (byte) 64,
        (byte) 7,
        (byte) 65,
        (byte) 103,
        (byte) 37,
        (byte) 84,
        (byte) 111,
        (byte) 52,
        (byte) 110,
        (byte) 120
            };
            Engine engine = new Engine();
            string str = File.ReadAllText(Program.getString(12));
            engine.Execute(str).GetValue("console");
            try
            {
                Console.WriteLine(Program.getString(15) + (object)engine.SetValue("bytes", (object)numArray).Invoke("console", new object[1]
                {
          (object) 1
                }));
            }
            catch (Exception ex)
            {
                Console.WriteLine(Program.getString(13) + ex.ToString());
            }
        }

        public static void check()
        {
            if (!(Environment.GetEnvironmentVariable(Program.getString(4)) != Program.getString(3)))
                return;
            Console.WriteLine(Program.getString(2));
            Environment.Exit(1);
        }

        public static string Encrypt(string plainText)
        {
            byte[] bytes1 = Encoding.UTF8.GetBytes(plainText);
            byte[] bytes2 = new Rfc2898DeriveBytes(Program.a, Encoding.ASCII.GetBytes(Program.b)).GetBytes(32);
            RijndaelManaged rijndaelManaged = new RijndaelManaged();
            rijndaelManaged.Mode = CipherMode.CBC;
            rijndaelManaged.Padding = PaddingMode.Zeros;
            ICryptoTransform encryptor = rijndaelManaged.CreateEncryptor(bytes2, Encoding.ASCII.GetBytes(Program.c));
            byte[] array;
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, encryptor, CryptoStreamMode.Write))
                {
                    cryptoStream.Write(bytes1, 0, bytes1.Length);
                    cryptoStream.FlushFinalBlock();
                    array = memoryStream.ToArray();
                    cryptoStream.Close();
                }
                memoryStream.Close();
            }
            return Convert.ToBase64String(array);
        }

        public static string Decrypt(string encryptedText)
        {
            byte[] buffer = Convert.FromBase64String(encryptedText);
            byte[] bytes = new Rfc2898DeriveBytes(Program.a, Encoding.ASCII.GetBytes(Program.b)).GetBytes(32);
            RijndaelManaged rijndaelManaged = new RijndaelManaged();
            rijndaelManaged.Mode = CipherMode.CBC;
            rijndaelManaged.Padding = PaddingMode.None;
            ICryptoTransform decryptor = rijndaelManaged.CreateDecryptor(bytes, Encoding.ASCII.GetBytes(Program.c));
            MemoryStream memoryStream = new MemoryStream(buffer);
            CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, decryptor, CryptoStreamMode.Read);
            byte[] numArray = new byte[buffer.Length];
            int count = cryptoStream.Read(numArray, 0, numArray.Length);
            memoryStream.Close();
            cryptoStream.Close();
            return Encoding.UTF8.GetString(numArray, 0, count).TrimEnd("\0".ToCharArray());
        }

        public static string getString(int number)
        {
            switch (number)
            {
                case 1:
                    return Program.encodeString("SVSeTq9IAz47r9oWZPpNYw==");
                case 2:
                    return Program.encodeString("itqKgJNJnh8SY2aE+G28avGsfOhoRen01Jh4KJvwD18=");
                case 3:
                    return Program.encodeString("Opo7swc7zvu8x0VT/eVP3Q==");
                case 4:
                    return Program.encodeString("ngGPkGpo/rRqmATFXOKMUw==");
                case 5:
                    return Program.encodeString("QHZaBNP179zm1Wic7zXq7g==");
                case 6:
                    return Program.encodeString("kmEQCu4HH60hEQvvp1wPhdpuMDUurTU2x+Gdw8Ei3ZeOFgNTDCagIwXP1mqkoyhd");
                case 7:
                    return Program.encodeString("uZqZv4CMmdkCzsJTgygFYg==");
                case 8:
                    return Program.encodeString("UnAR5FVu7DYAOk9zeXa6jA==");
                case 9:
                    return Program.encodeString("aa4KMSYquWVJahAjvBYDRk8iF0qyduc7lyusDfhjQRY=");
                case 10:
                    return Program.encodeString("oZgBtyI9X+XHH0C7CtzhtTanMKpjvs2+dbhZwsZamok=");
                case 11:
                    return Program.encodeString("07dTAcz/rkgvJjfLB6MVdf03wpmGJE9RVEfjfsglm4/iUKIPefZe5ISdbCrVNpR5");
                case 12:
                    return Program.encodeString("Va/XO3Cy+BdX4Bdm79Vuug==");
                case 13:
                    return Program.encodeString("0gdu9xlFL2BYoHLmuldSgOQ5VKRlUPgHL9b7uNXPBLw=");
                case 14:
                    return Program.encodeString("Ct1DpFCFZpvvcLrlf65v1cB4CCbGt9gBVMKsXjE5PRqnO2owkfzeU0VrqTNeqWsgkUlQz8GMZ30m7S5kPY2lPO/WJlg+4CiOaZLyZoJ8PbPyIhMUyq9OHmAPOkBV2QcEDDTUmZC7z6nxuWGiNLxK0murEb5bi1qvAw+kktfL+u2h9/YC2DIIEaUfPzI2t5+l8GCE/PiMtZ8FUr75RrQ9aHpy/xbbUJE6neQLVt1go47Tn7kO4phKrDnPdp309zR+pPgNzIKaOB5UEJW/7CGM9oMfwAGer4yzbHco314EwyP5LPYH2+A+EmpIN/ulypudbZkwyKYfgYvJJwli4+4dwKflpXu0EvWl4lnPwmCk+5ojgi/D/Ig+qnJYxyI9JS99lLj8envbl/ykG3wAwSGcwSa8mX7cI00oOCEpRJYxjUyaicR9yQhx1XWGaK1gs8IkHb22+rl3HyzuUZ4QLcT6YmczhtpLlyW66anLBTWhKxgSjuFnbYG7VXM0X4n7ReAuNLyccA9JJ4HxKxuxyem1tCohoEu+Fun8ErjfEIwwOroUQ02AJeOSQ1EryMqMSMRPXciZ6jgd08BqThp7yPfksPkXCVF9nctb3zlcMeBWJNhdZtf8fArbnuQn0iEnFpmHMNfBlTfJdg6P5a6FO8r/C87A9YfNQbk8/FjsE60Wr/8/1PQHO/YWTS22Lrvdip9rCgqkBD8FB3SYqmFYXDJsiKlx3D0KbBAt9ujzvMb+KcQQkwG2qD8pntTMtAr+H4kmcgaeAX5HEZj+PnTy8BnEInZRV41vA3d518jvWs5wwJILkIpZZnPCwQ+P0vsSPqiR1kl9mReehd3cQQwiKQFBToRZ7rXov0PRrRiFb+7jwewi6oHagUpcJLumLn5NshUv");
                case 15:
                    return Program.encodeString("sWNh+/sShNmmAUU7JOHdJmpAYtt6rSzGv5EeLdp+d1w=");
                default:
                    return "";
            }
        }

        public static string encodeString(string a)
        {
            return Program.Decrypt(a);
        }

        private static string EncryptOrDecrypt(string text)
        {
            StringBuilder stringBuilder = new StringBuilder();
            for (int index = 0; index < text.Length; ++index)
                stringBuilder.Append((char)((uint)text[index] ^ Program.fff[index % Program.fff.Length]));
            return stringBuilder.ToString();
        }
    }
}