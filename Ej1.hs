import Data.List

-- Definir la lista de diccionarios
d :: [[(String, String)]]
d = [ [("make", "Nokia"), ("model", "216"), ("color", "Black")]
    , [("make", "Apple"), ("model", "2"), ("color", "Silver")]
    , [("make", "Huawei"), ("model", "50"), ("color", "Gold")]
    , [("make", "Samsung"), ("model", "7"), ("color", "Blue")]
    ]

-- Clave para ordenar la lista de diccionarios
keyToSort :: String
keyToSort = "model"

-- Función para ordenar la lista de diccionarios con respecto a la clave indicada
sortList :: String -> [[(String, String)]] -> [[(String, String)]]
sortList key list = sortBy (\x y -> compare (lookup key x) (lookup key y)) list

-- Imprimir la lista ordenada
main :: IO ()
main = mapM_ print (sortList keyToSort d)
