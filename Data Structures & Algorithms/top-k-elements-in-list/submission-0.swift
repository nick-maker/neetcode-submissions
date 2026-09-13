class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dict = [Int: Int]()
        for num in nums {
            dict[num, default: 0] += 1
        }

        return dict.sorted {
            ($0.value, $0.key) > ($1.value, $1.key)
        }.prefix(k).map { $0.key } 

    }
}
